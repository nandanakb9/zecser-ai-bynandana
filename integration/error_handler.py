# Error Handling & Retry Logic

def handle_api_error(api_name, retries=3):

    attempt = 0

    while attempt < retries:

        attempt += 1

        print(f"Retrying {api_name}... Attempt {attempt}")

    return {
        "api": api_name,
        "status": "failed_after_retry"
    }


def validate_payload(payload):

    if not payload:
        return False

    return True