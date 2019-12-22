""" run script to return input keyword matches

dependencies(pip):
==================
pip install --upgrade 'algoliasearch>=2.0,<3.0'
pip install 'asyncio>=3.4,<4.0' 'aiohttp>=2.0,<4.0' 'async_timeout>=2.0,<4.0'

"""
import urllib.request
import json

from algoliasearch.search_client import SearchClient

# Free Public limited key (14 days)
client = SearchClient.create('2HQFIEJLUM', 'enter your key')
index = client.init_index('contacts')

# Call http request method with urllib
with urllib.request.urlopen(
        "https://raw.githubusercontent.com/algolia/datasets/master/contacts"
        "/contacts.json") as url:
    # get json data
    batch = json.loads(url.read().decode())

    # save json data into algoliasearch
    index.save_objects(batch, {'autoGenerateObjectIDIfNotExist': True})

    # algolia search settings https://www.algolia.com/doc/guides/
    index.set_settings({
        'customRanking': ["desc(followers)"],
        'searchableAttributes': ["lastname", "firstname", "company",
                                 "email", "city", "address"],
        'attributesToRetrieve': [
            'firstname', 'lastname', 'phone', 'email', 'followers', 'company',
            'city', 'address'
        ],
        'attributeForDistinct': 'phone',
        'distinct': True,
        'hitsPerPage': 10
    })

print("Welcome to Personal Info Search API")
print("=========================")
print()


def main_program(algo):
    key_word = input("Enter keyword (eg. Jess): ")
    print()
    # try catch is a valid number
    try:
        ret = algo.search(str(key_word), {
            'distinct': 1
        })

        if 'hits' in ret.keys():
            if ret['nbHits'] == 0:
                print("No matches were found")

            for count, person in enumerate(ret['hits']):
                print(f"{count + 1}. ===============")

                print(f"    First Name = {person['firstname']}")
                print(f"    Last Name  = {person['lastname']}")
                print(f"    Phone      = {person['phone']}")
                print(f"    City       = {person['city']}")
                print(f"    Address    = {person['address']}")
                print(f"    Company    = {person['company']}")
                print()

        else:
            raise KeyError

        # is continue or exit program
        to_continue = input("Continue ? (y/n): ")
        print()
        if 'y' in to_continue.lower():
            main_program(algo)
        else:
            # Exit program
            print("Thank for using")
            return

    # somehow hits key not found for result result
    except KeyError:
        print("!!! Invalid API Result, Please Try Again !!!")
        main_program(algo)

    return


if __name__ == '__main__':
    main_program(index)
