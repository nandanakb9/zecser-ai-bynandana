import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from integration.api_endpoints import API_ENDPOINTS
from integration.api_schemas import ATS_RESPONSE
from integration.integration_flow import SYSTEM_FLOW
from integration.processing_modes import PROCESSING_MODES
from integration.auth_security import SECURITY_CONFIG


print("\nAPI ENDPOINTS\n")
print(API_ENDPOINTS)

print("\nATS RESPONSE SAMPLE\n")
print(ATS_RESPONSE)

print("\nSYSTEM FLOW\n")
print(SYSTEM_FLOW)

print("\nPROCESSING MODES\n")
print(PROCESSING_MODES)

print("\nSECURITY CONFIG\n")
print(SECURITY_CONFIG)