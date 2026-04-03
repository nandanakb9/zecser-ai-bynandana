from utils.logger import get_logger

logger = get_logger(__name__)

def test_ats():
    logger.info("ATS Test Started")
    print("ATS engine test running...")
    logger.info("ATS Test Completed")

if __name__ == "__main__":
    test_ats()