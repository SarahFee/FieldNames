# FieldNames
This script defines a Python program that is designed to convert a given sentence into a standardized field name, particularly useful for naming fields in forms, surveys, or databases, like Open Data Kit (ODK). The script also counts the number of characters in the generated field name. 

- sentence_to_odk_fieldname Function: This is the core function of the script. It takes a sentence and an answer type as inputs and processes the sentence to generate a field name according to specific rules. These rules include:

- Replacing Abbreviations: The function has a dictionary of abbreviations, which it uses to replace certain words or phrases in the sentence with their abbreviated forms.
- Processing Parentheses: Text within parentheses is included or excluded based on its character count (excluding punctuation). If the text is too long, it's excluded.
- Handling Special Characters: The function replaces certain characters, like '/', with underscores to make the text more suitable for a field name.
- Removing Irrelevant Words: Certain general and context-specific words are removed from the sentence.
- Lowercasing and Splitting: The sentence is converted to lowercase and split into words.
- Creating Field Name: The remaining words are then combined to form a field name, following specific rules based on the answer type (e.g., 'select_one', 'decimal').
main Function: This is a higher-level function that uses sentence_to_odk_fieldname. It:

- Takes a sentence and an answer type.
- Calls sentence_to_odk_fieldname to generate a field name.
- Calculates the character count of the generated field name.
- Returns both the field name and its character count.

In summary, this script is designed to automate the conversion of sentences into standardized field names, considering various linguistic and formatting rules. It's particularly useful in contexts where consistent and clear field naming is crucial, such as in data collection tools and databases.
[Try it out yourself](https://huggingface.co/spaces/Sfe61/FieldNames_Standardization)

1) Enter your Indicator in  Enter Sentence
2) Select the Answer Type
3) Submit
4) Field Name section will display the generated FieldName
5) Charcters Count will display the count of Charcters (the script is made so that it is always less than 128)


