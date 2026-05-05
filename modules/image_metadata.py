#!/usr/bin/env python3
"""
🦅 Dark Eagle - Image Metadata Extraction & Analysis
"""

import sys
import os
import json
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import argparse

console = Console()

class ImageMetadata:
    def __init__(self):
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.webp']
    
    def convert_to_serializable(self, value):
        if hasattr(value, 'numerator') and hasattr(value, 'denominator'):
            return float(value.numerator / value.denominator) if value.denominator != 0 else 0
        elif isinstance(value, bytes):
            return value.decode('utf-8', errors='ignore')
        elif isinstance(value, tuple):
            return list(value)
        elif isinstance(value, (int, float, str, bool)):
            return value
        elif value is None:
            return None
        else:
            return str(value)
    
    def extract_exif(self, image_path):
        console.print(f"\n[bold cyan]📸 Analyzing Image: {image_path}[/]")
        
        if not os.path.exists(image_path):
            console.print(f"[red]❌ File not found: {image_path}[/]")
            return None
        
        exif_data = {}
        
        try:
            image = Image.open(image_path)
            
            exif_data['File'] = {
                'Name': os.path.basename(image_path),
                'Size': f"{os.path.getsize(image_path) / 1024:.2f} KB",
                'Format': image.format,
                'Dimensions': f"{image.width} x {image.height}",
                'Mode': image.mode
            }
            
            exif = image._getexif()
            
            if exif:
                for tag_id, value in exif.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == 'GPSInfo':
                        gps_data = {}
                        for gps_tag in value:
                            sub_tag = GPSTAGS.get(gps_tag, gps_tag)
                            gps_data[sub_tag] = self.convert_to_serializable(value[gps_tag])
                        exif_data['GPS'] = self.convert_gps(gps_data)
                    else:
                        exif_data[tag] = self.convert_to_serializable(value)
            else:
                console.print("[yellow]⚠️ No EXIF metadata found[/]")
                
        except Exception as e:
            console.print(f"[red]Error: {e}[/]")
            return None
        
        return exif_data
    
    def convert_gps(self, gps_data):
        try:
            lat = gps_data.get('GPSLatitude')
            lon = gps_data.get('GPSLongitude')
            lat_ref = gps_data.get('GPSLatitudeRef', 'N')
            lon_ref = gps_data.get('GPSLongitudeRef', 'E')
            
            if lat and lon:
                lat_decimal = self._convert_to_decimal(lat)
                lon_decimal = self._convert_to_decimal(lon)
                
                if lat_ref == 'S':
                    lat_decimal = -lat_decimal
                if lon_ref == 'W':
                    lon_decimal = -lon_decimal
                
                return {
                    'Latitude': f"{lat_decimal:.6f}°",
                    'Longitude': f"{lon_decimal:.6f}°",
                    'Google Maps': f"https://maps.google.com/?q={lat_decimal},{lon_decimal}",
                    'OpenStreetMap': f"https://www.openstreetmap.org/?mlat={lat_decimal}&mlon={lon_decimal}"
                }
        except:
            pass
        return None
    
    def _convert_to_decimal(self, coordinate):
        if isinstance(coordinate, (int, float)):
            return float(coordinate)
        try:
            if hasattr(coordinate, 'numerator'):
                return float(coordinate.numerator / coordinate.denominator) if coordinate.denominator != 0 else 0
        except:
            pass
        return 0.0
    
    def reverse_image_search(self, image_path):
        console.print(f"\n[bold cyan]🔍 Reverse Image Search for: {image_path}[/]")
        console.print("[yellow]Upload to these services for reverse search:[/]")
        console.print("  • Google Images: https://images.google.com/")
        console.print("  • TinEye: https://tineye.com/")
        console.print("  • Yandex: https://yandex.com/images/")
        return []
    
    def display_metadata(self, exif_data):
        if not exif_data:
            return
        
        console.print("\n[bold green]📊 Image Metadata Report[/]\n")
        
        if 'File' in exif_data:
            file_table = Table(title="File Information")
            file_table.add_column("Property", style="cyan")
            file_table.add_column("Value", style="white")
            for key, value in exif_data['File'].items():
                file_table.add_row(key, str(value))
            console.print(file_table)
        
        camera_keys = ['Make', 'Model', 'DateTime', 'DateTimeOriginal', 'ExposureTime', 
                      'FNumber', 'ISOSpeedRatings', 'FocalLength', 'Flash', 'Artist', 'Copyright']
        
        camera_data = {}
        for key in camera_keys:
            if key in exif_data:
                camera_data[key] = exif_data[key]
        
        if camera_data:
            camera_table = Table(title="Camera Information")
            camera_table.add_column("Property", style="cyan")
            camera_table.add_column("Value", style="white")
            for key, value in camera_data.items():
                camera_table.add_row(key, str(value))
            console.print(camera_table)
        
        if 'GPS' in exif_data and exif_data['GPS']:
            gps_data = exif_data['GPS']
            gps_table = Table(title="📍 GPS Location Data")
            gps_table.add_column("Property", style="cyan")
            gps_table.add_column("Value", style="white")
            for key, value in gps_data.items():
                gps_table.add_row(key, str(value))
            console.print(gps_table)
    
    def analyze(self, image_path, interactive=True):
        exif_data = self.extract_exif(image_path)
        
        if exif_data:
            self.display_metadata(exif_data)
            
            if interactive:
                console.print("\n[bold yellow]Perform reverse image search? (y/n)[/]")
                choice = input("> ")
                if choice.lower() == 'y':
                    self.reverse_image_search(image_path)
            
            report = {
                'image': image_path,
                'timestamp': datetime.now().isoformat(),
                'metadata': exif_data
            }
            
            report_file = f"image_report_{os.path.basename(image_path)}.json"
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            
            console.print(f"\n[green]✅ Report saved: {report_file}[/]")
            return exif_data
        else:
            console.print("[red]❌ Failed to extract metadata[/]")
            return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract image metadata")
    parser.add_argument("image", help="Path to image file")
    parser.add_argument("--no-interactive", action="store_true", help="Skip interactive prompts")
    args = parser.parse_args()
    
    analyzer = ImageMetadata()
    analyzer.analyze(args.image, interactive=not args.no_interactive)
