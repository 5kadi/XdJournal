
/*
const TEMPLATES: [RegExp, string][] = [
    [/[*]{2}(.*?)[*]{2}/gm, '<b>$1</b>'], //bold
    [/[~]{2}(.*?)[~]{2}/gm, '<i>$1</i>'], //cursive
    
    [/[#]{4}(.*?)[#]{4}/, '<h2>$1</h2>'], //headers (more # -> higher priority)
    [/[#]{3}(.*?)[#]{3}/, '<h3>$1</h3>'],
    [/[#]{2}(.*?)[#]{2}/, '<h4>$1</h4>'],
]

export function replaceMarkdown(text: string) {
    let replacedText = text
    for (const T of TEMPLATES) {
        replacedText = replacedText.replace(T[0], T[1])
    }
    return replacedText
} */


export function generateId(){
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}






