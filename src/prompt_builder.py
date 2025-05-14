def build_prompt(question: str, context: str, doc_type: str, instructions: dict = None) -> str:
    def clean_context(text: str) -> str:
        import unicodedata, re
        text = unicodedata.normalize("NFKC", text)
        text = text.replace("ﬁ", "fi").replace("●", "-").replace("–", "-")
        return re.sub(r"[^\x00-\x7FğüşıöçĞÜŞİÖÇ\s\w,.!?;:()\-]", "", text).strip()

    def truncate_context(text: str, max_chars=3000) -> str:
        return text[:max_chars] + "..." if len(text) > max_chars else text

    context = truncate_context(clean_context(context))

    base_instruction = (
        "Aşağıda verilen içerik, belirli bir belgeye aittir. Lütfen sadece bu içerikte yer alan bilgilere dayanarak "
        "cevap üret. Cevabın açık, sade ve Türkçe olmalı. Ekstra yorum, tahmin, çıkarım veya uydurma bilgi ekleme."
    )

    type_instruction = (
        instructions.get(doc_type)
        if instructions and doc_type in instructions
        else "Bu belge genel bir içerik sunar. Belirli bir yapısı olmayabilir. Soruyu sadece verilen metindeki bilgilere dayanarak, açık ve doğru şekilde cevapla."
    )

    return f"""{base_instruction}

Belge tipi açıklaması:
{type_instruction}

Belge içeriği:
{context}

Soru: {question}
Cevap:"""
