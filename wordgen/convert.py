# -*- coding: utf-8 -*-
"""Convert pipe-delimited word data to words.json"""
import json, os

def parse_words(text, lang):
    """Parse pipe-delimited word data into list of dicts"""
    words = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) >= 7:
            words.append({
                'w': parts[0].strip(),
                'm': parts[1].strip(),
                'p': parts[2].strip(),
                'ex': parts[3].strip(),
                'ec': parts[4].strip(),
                'cat': parts[5].strip(),
                'lv': parts[6].strip(),
                'lang': lang
            })
    return words

def main():
    all_words = []
    data_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Read all part files
    for fname in sorted(os.listdir(data_dir)):
        if fname.startswith('data_') and fname.endswith('.txt'):
            fpath = os.path.join(data_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Extract language from filename: data_en_core.txt -> en
            parts = fname.replace('.txt','').split('_')
            lang = parts[1]  # 'en' or 'ru'
            words = parse_words(content, lang)
            all_words.extend(words)
            print(f"  {fname}: {len(words)} words")
    
    # Remove duplicates (keep first occurrence)
    seen = set()
    unique = []
    for w in all_words:
        key = f"{w['lang']}_{w['w'].lower()}"
        if key not in seen:
            seen.add(key)
            unique.append(w)
    
    print(f"\nTotal unique words: {len(unique)}")
    
    # Split by language
    en_words = [w for w in unique if w['lang'] == 'en']
    ru_words = [w for w in unique if w['lang'] == 'ru']
    print(f"  English: {len(en_words)}")
    print(f"  Russian: {len(ru_words)}")
    
    # Count by level
    for lang_name, lang_words in [('English', en_words), ('Russian', ru_words)]:
        for lv in ['core', 'intermediate', 'advanced']:
            count = len([w for w in lang_words if w['lv'] == lv])
            print(f"  {lang_name} {lv}: {count}")
    
    # Output
    output = {
        'version': '1.0',
        'generated': '2026-07-29',
        'en': en_words,
        'ru': ru_words
    }
    
    out_path = os.path.join(data_dir, '..', 'words.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=1)
    
    print(f"\nWritten to: {out_path}")
    print(f"File size: {os.path.getsize(out_path)} bytes")

if __name__ == '__main__':
    main()
