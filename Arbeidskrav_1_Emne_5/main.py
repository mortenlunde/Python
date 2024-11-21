from datetime import datetime
from Arbeidskrav_1_Emne_5.Contact import Contact
from Arbeidskrav_1_Emne_5.Phonebook import Phonebook

def main():
    phonebook = Phonebook()

    phonebook.add_contact(Contact("Morten", "Lunde", "455-123-456", datetime(1990, 10, 30), "Luna 42", "The Moon"))
    phonebook.import_contacts_from_jsonl_file("People.jsonl")

    print("Displaying all contacts:")
    print(phonebook.display_all_contacts())

    print("\nDisplaying contact number 50:")
    print(phonebook[50].display())

    print("\nSearching for contact(s) that includes the text '197':")
    search_result = phonebook.search_contact("197")
    if search_result:
        print(search_result)

    print("")
    valid_sort = phonebook.sort_contacts("birthday", "asc")
    if valid_sort:
        print(phonebook.display_all_contacts())

if __name__ == '__main__':
    main()