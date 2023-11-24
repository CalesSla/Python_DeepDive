template = {
    'user_id': int,
    'name': str,
    "address": {
        "street": str,
        "house": int,
        "location": {
            "street": str,
            "ap": int
        }
    }
}

olia = {
    "user_id": 1,
    "name": "olia",
    "address": {
        "street": "Mircea",
        "house": 3,
        "location": {
            "street": "cuza",
            # "ap": 56
        }
    }
}



def validate(data, template, is_recursive, missing_from_data=None, missing_from_template=None):
    if missing_from_data is None:
        missing_from_data = ""
    if missing_from_template is None:
        missing_from_template = ""
    
    
    if data.keys() ^ template.keys() != set():
        missing_field = (template.keys() - data.keys())
        if missing_field:
            missing_from_data += "." + missing_field.pop()
        else:
            missing_from_template += "." + (data.keys() - template.keys()).pop()
        
        if not is_recursive:
            if missing_from_data:
                print("The following data is missing: template"+missing_from_data)
            elif missing_from_template:
                print(f"The template does not have" + " template"+missing_from_template)
        
        return False, missing_from_data, missing_from_template

    else:
        for k, v in template.items():
            if type(v) == dict:
                inter_res, missing_from_data, missing_from_template = validate(data=data[k], template=v, is_recursive=True, missing_from_data=missing_from_data, missing_from_template=missing_from_template)
                break
                if not inter_res:
                    if missing_from_data:
                        print("The following data is missing: template"+missing_from_data)
                    elif missing_from_template:
                        print(f"The template does not have" + " template"+missing_from_template)
                    return False, missing_from_data, missing_from_template
                
            elif type(data[k]) != v:
                print("======================")
                print(f"Expected: {k, v}\nactual: {type(data[k])}")
                print("======================")
                return False, missing_from_data, missing_from_template
      
    return True, missing_from_data, missing_from_template
                


validate(olia, template, False)