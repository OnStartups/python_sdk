from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def convert_file_workflow(input_file_url, target_extension="txt"):
    print(f"Converting file from URL: {input_file_url} to extension: {target_extension}\n")

    # 1. Get Convert File Options (to validate target_extension)
    print("--- Fetching convertible extensions... ---")
    options_response = client.action(
        action_id="convertFileOptions",
        params={"extension": "pdf"} # Assuming input is PDF for this example, adjust if needed
    )

    if options_response['status'] == 200:
        convertible_extensions = options_response['results']
        print(f"File format options fetched: {convertible_extensions}")

        if target_extension not in convertible_extensions:
            print(f"Error: Cannot convert to '{target_extension}'. Valid options are: {convertible_extensions}")
            return {"conversion_status": "failed", "error_message": f"Invalid target extension: {target_extension}"}

        # 2. Convert File
        print(f"--- Converting file to '{target_extension}'... ---")
        convert_response = client.action(
            action_id="convertFile",
            params={"input_file": input_file_url, "convert_to_extension": target_extension}
        )

        if convert_response['status'] == 200:
            converted_files = convert_response['results']
            if converted_files and converted_files[0].get('url'):
                converted_url = converted_files[0]['url']
                print(f"File converted successfully. Converted file URL: {converted_url}")
                return {"conversion_status": "success", "converted_url": converted_url}
            else:
                error_message = "Conversion successful, but no file URL returned."
                print(error_message)
                return {"conversion_status": "failed", "error_message": error_message}

        else:
            error_message = f"File conversion failed: {convert_response['error']}"
            print(error_message)
            return {"conversion_status": "failed", "error_message": error_message}

    else:
        error_message = f"Error fetching convertible extensions: {options_response['error']}"
        print(error_message)
        return {"conversion_status": "failed", "error_message": error_message}


if __name__ == "__main__":
    file_to_convert_url = "https://www.irs.gov/pub/irs-pdf/fw4.pdf" # Example PDF file URL
    output_file_extension = "txt" # Convert to TXT format

    conversion_result = convert_file_workflow(file_to_convert_url, output_file_extension)

    if conversion_result['conversion_status'] == "success":
        print("\nFile Conversion Workflow Result:")
        print("Conversion Status: Success")
        print("Converted File URL:", conversion_result['converted_url'])
    else:
        print("\nFile Conversion Workflow Failed:")
        print("Conversion Status: Failed")
        print("Error Message:", conversion_result['error_message'])
