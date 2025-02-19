from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def enrich_lead_data(company_domain, linkedin_profile_handle=None):
    print(f"Enriching lead data for domain: {company_domain}\n")

    # 1. Get Company Object
    print("--- Fetching company object... ---")
    company_response = client.action(action_id="getCompanyObject", params={"domain": company_domain})

    if company_response['status'] == 200:
        print("Company object fetched successfully.")
        company_data = company_response['results']
        company_description = company_data.get('description', 'No company description available.')
        company_industry = company_data['category'].get('industry', 'Industry not specified') if company_data.get('category') else 'Category data not available.'
        company_employee_range = company_data['metrics'].get('employeesRange', 'Employee range not available') if company_data.get('metrics') else 'Metrics data not available.'

        print(f"Company Description: {company_description[:500]}...\n")
        print(f"Industry: {company_industry}")
        print(f"Employee Range: {company_employee_range}\n")

    else:
        print(f"Error fetching company object: {company_response['error']}")
        company_description = f"Error fetching company data: {company_response['error']}"
        company_industry = "N/A"
        company_employee_range = "N/A"

    # 2. Get LinkedIn Profile (optional, if handle is provided)
    if linkedin_profile_handle:
        print("--- Fetching LinkedIn profile... ---")
        linkedin_response = client.action(action_id="getLinkedinProfile", params={"profile_handle": linkedin_profile_handle})
        if linkedin_response['status'] == 200:
            print("LinkedIn profile data retrieved.")
            linkedin_profile_data = linkedin_response['results']['response']
            linkedin_followers = linkedin_profile_data['network_info'].get('followers_count', 'Follower count not available.') if linkedin_profile_data.get('network_info') else 'Network info not available.'
            linkedin_industry = linkedin_profile_data.get('industry', 'Industry not available on LinkedIn profile.')
            linkedin_location = linkedin_profile_data['location'].get('default', 'Location not available.') if linkedin_profile_data.get('location') else 'Location data not available.'

            print(f"LinkedIn Followers: {linkedin_followers}")
            print(f"LinkedIn Industry: {linkedin_industry}")
            print(f"LinkedIn Location: {linkedin_location}\n")
        else:
            print(f"Error fetching LinkedIn profile: {linkedin_response['error']}")
            linkedin_followers = "Error fetching LinkedIn data."
            linkedin_industry = "N/A"
            linkedin_location = "N/A"
    else:
        linkedin_followers = "LinkedIn profile enrichment skipped."
        linkedin_industry = "N/A"
        linkedin_location = "N/A"
        print("Skipping LinkedIn profile enrichment (no handle provided).\n")


    print("--- Lead Enrichment Complete ---")
    return {
        "company_description": company_description,
        "company_industry": company_industry,
        "company_employee_range": company_employee_range,
        "linkedin_followers": linkedin_followers,
        "linkedin_industry": linkedin_industry,
        "linkedin_location": linkedin_location
    }


if __name__ == "__main__":
    lead_domain = "hubspot.com" # Example company domain
    lead_linkedin_handle = "company/hubspot" # Example LinkedIn company handle (optional)

    enrichment_result = enrich_lead_data(lead_domain, lead_linkedin_handle)

    # You can save this enriched data to your CRM or database
    print("\nEnrichment Result:")
    print(enrichment_result)
