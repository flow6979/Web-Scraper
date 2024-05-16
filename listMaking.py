import json

class JSONProcessor:
    def __init__(self, json_file_path, output_file_path):
        self.json_file_path = json_file_path
        self.output_file_path = output_file_path

    def process_and_save(self):
        try:
            # Read the JSON content
            with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            # Extract data from "getRecommendedMerchantsV2" and "getRestaurantsV2"
            recommended_merchants = data.get("getRecommendedMerchantsV2/countryCode=SG&latitude=1.287953&longitude=103.851784", {}).get("getRecommendedMerchantsV2/countryCode=SG&latitude=1.287953&longitude=103.851784", [])
            restaurant_list = data.get("getRestaurantsV2/countryCode=SG&latlng=1.287953%2C103.851784", {}).get("getRestaurantsV2/countryCode=SG&latlng=1.287953%2C103.851784", [])

            combined_list = recommended_merchants + restaurant_list

            print("Combined List Array:", combined_list)

            # Store the combined list as a JSON array in a text file
            with open(self.output_file_path, 'w', encoding='utf-8') as output_file:
                json.dump(combined_list, output_file, indent=2)

            print(f"Combined list stored in '{self.output_file_path}'")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        except FileNotFoundError:
            print(f"Error: File not found at path '{self.json_file_path}'")

json_file_path = r'combined_list.txt'
output_file_path = r'combined_listArray.txt'

json_processor = JSONProcessor(json_file_path, output_file_path)
json_processor.process_and_save()
