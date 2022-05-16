from scripts import sentinel_data_download
from datetime import date
import os
start_date = date(2022,5,12)
end_date = date(2022,5,13)
download_path = "data/sentinel_data_download"
os.makedirs(download_path, exist_ok=True)
sentinel_data_download.main("data/bbox.geojson",start_date=start_date, end_date=end_date, platform="Sentinel-2", username="rszostak", password=r"mhpt%6ekbp", download_path=download_path, download_images=True, cloud_cover_percentage=100, limit_tiles=[])