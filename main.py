import os
import pymediumapi


def main():
    client = pymediumapi.Client(os.environ.get('MEDIUM_INTEGRATION_TOKEN'))
    
    try:
        client.authenticate()
    except Exception as e:
        print("Failed authentication: " + str(e))
        quit()

    try:
        pubblications = client.get_pubblications()
    except Exception as e:
        print("Failed get pubblications: " + str(e))
        quit()

    if pubblications:
        pub_id = pubblications[0]["id"]
        
        try:
            contributors = client.get_contributors(pub_id)
        except Exception as e:
            print("Failed getting contributors: " + str(e))
        else:
            print(contributors)
    else:
        print("There are no pubblications")
        quit()


if __name__ == "__main__":
    main()