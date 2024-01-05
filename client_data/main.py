from client_data.cats_client import CatsClient
from client_data.email_verification_service import EmailVerificationService


def main():
    cats_client = CatsClient()
    cat = cats_client.get_random_cat_image()
    print(f"Random Joke: {cat}")

    email_service = EmailVerificationService()
    email = "example@email.com"
    verification_result = email_service.verify_email(email)
    print(f"Email Verification Result: {verification_result}")

    all_results = email_service.get_all_results()
    print(f"All Email Verification Results: {all_results}")


if __name__ == "__main__":
    main()
