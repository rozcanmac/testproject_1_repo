import re
from typing import Dict

def fix_typos(doc: str) -> str:
    """
    This function takes in a string representing documentation and fixes common typos.
    
    Args:
        doc (str): The input documentation to be processed
    
    Returns:
        str: The processed documentation with fixed typos
    """
    # Define a dictionary of typo replacements
    typo_replacements: Dict[str, str] = {
        "accomodate": "accommodate",
        "indescrishible": "indescribable",
        "seperation": "separation",
        # Add more typo replacements as needed
    }
    
    # Use regular expressions to replace typos in the documentation
    for old, new in typo_replacements.items():
        doc = re.sub(r'\b' + re.escape(old) + r'\b', new, doc)
    
    return doc

# Example usage:
doc = "The accomodate changes are indescrishible. We need a good seperation between sections."
processed_doc = fix_typos(doc)
print(processed_doc)