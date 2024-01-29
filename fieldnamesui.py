import gradio as gr
import re

def sentence_to_odk_fieldname(sentence, answer_type):
    # Dictionary for specific abbreviations
    abbreviations = {
        '%': 'percentage',
        'internally displaced peoples': 'idps',
        'minors under the age of 18': 'minors',
        'minors under 18 years': 'minors',
        'key informant':'ki',
        'households': 'hh',
    }

    # Process text within parentheses
    def include_or_exclude(match):
        text = match.group(0)
        char_count = len(re.sub(r'[^\w\s]', '', text))  # Count characters excluding punctuation
        return text if char_count <= 20 else ''

    # Handle '/' character within words
    sentence = re.sub(r'\b/\b', '_', sentence)

    # Apply the logic for text within parentheses
    sentence = re.sub(r'\([^)]*\)', include_or_exclude, sentence)

    general_words_to_remove = {'do', 'you', 'to', 'your', 'a', 'the', 'is', 'are', 'of', 'in', 'this'}
    measurement_words = {'average', 'total', 'sum', 'count', 'maximum', 'minimum'}

    if answer_type in ['select_one', 'select_multiple']:
        additional_words_to_remove = {'what', 'which', 'who', 'how', 'why', 'did'}
    else:
        additional_words_to_remove = set()

    words_to_remove = general_words_to_remove.union(additional_words_to_remove)
    sentence = sentence.lower()

    for key, value in abbreviations.items():
        sentence = sentence.replace(key, value)

    words = ''.join(char for char in sentence if char.isalnum() or char.isspace()).split()
    filtered_words = [word for word in words if word not in words_to_remove]

    if answer_type in ['decimal', 'integer']:
        field_name_parts = [word for word in filtered_words if word in measurement_words or word not in measurement_words]
    else:
        entity, context = None, []
        for word in filtered_words:
            if not entity:
                entity = word
            else:
                context.append(word)
        field_name_parts = [entity] if entity else []
        if context:
            field_name_parts.append('_'.join(context))

    field_name = '_'.join(field_name_parts)
    field_name = re.sub('_+', '_', field_name)
    field_name = field_name[:128]

    return field_name

def main(sentence, answer_type):
    field_name = sentence_to_odk_fieldname(sentence, answer_type)
    character_count = len(field_name)
    return field_name, character_count

answer_types = ["select_one", "select_multiple", "decimal", "integer", "text"]
iface = gr.Interface(
    fn=main, 
    inputs=[
        gr.Textbox(label="Enter Sentence"), 
        gr.Dropdown(choices=answer_types, label="Answer Type")
    ], 
    outputs=[
        gr.Textbox(label="Field Name"),
        gr.Textbox(label="Character Count")
    ]
)

iface.launch()