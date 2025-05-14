def build_prompt(question: str, context: str, doc_type: str) -> str:
    if doc_type == "resume":
        return f"""Aşağıda bir özgeçmiş belgesi var. Kullanıcının sorusunu bu kişiye dair bilgileri kullanarak cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "academic":
        return f"""Aşağıda bir akademik çalışma var. Bu belgeye göre bilimsel, doğru ve açık şekilde soruyu yanıtla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "contract":
        return f"""Aşağıda bir sözleşme metni var. Bu belgeye dayanarak yasal ve net şekilde soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "transcript":
        return f"""Aşağıda bir not döküm belgesi var. Bu belgeye göre akademik başarıyla ilgili soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "invoice":
        return f"""Aşağıda bir fatura bilgisi yer alıyor. Bu belgeye göre tutar, ürün ve vergi gibi konuları açıklayarak soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "quotation":
        return f"""Aşağıda bir fiyat teklifi belgesi var. Maliyet, ürün ve fiyat bilgilerini kullanarak soruyu açıkla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "report":
        return f"""Aşağıda bir analiz/rapor belgesi var. Bulgular ve çıkarımları dikkate alarak soruyu yanıtla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "certificate":
        return f"""Aşağıda bir sertifika veya başarı belgesi yer alıyor. Bu belgeye göre soruyu açıkla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "application":
        return f"""Aşağıda bir başvuru veya dilekçe yer alıyor. Bu metne göre resmi ve açıklayıcı bir cevap ver:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "identity_document":
        return f"""Aşağıda bir kimlik belgesi yer alıyor. Bu belgeye dayanarak soruyu açıkla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "meeting_minutes":
        return f"""Aşağıda bir toplantı tutanağı yer alıyor. Katılımcılar, gündem ve kararları dikkate alarak cevap ver:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "financial":
        return f"""Aşağıda bir mali tablo yer alıyor. Gelir, gider ve bilançoyu dikkate alarak soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "manual":
        return f"""Aşağıda bir kullanım kılavuzu yer alıyor. Teknik detaylara ve işlevlere dayanarak soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "timesheet":
        return f"""Aşağıda bir çalışma çizelgesi var. Personel ve çalışma saatlerine göre soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "agenda":
        return f"""Aşağıda bir toplantı gündemi yer alıyor. Görüşülecek konulara göre soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "press_release":
        return f"""Aşağıda bir basın bülteni yer alıyor. Bu duyurunun içeriğine göre kamuya açık ve bilgilendirici cevap ver:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "legal_notice":
        return f"""Aşağıda bir hukuki bildirim yer alıyor. Resmi ve yasal açıklamalarla soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "presentation":
        return f"""Aşağıda bir sunum içeriği var. Görsel anlatım ve açıklamalara göre soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    elif doc_type == "marketing":
        return f"""Aşağıda bir pazarlama veya ürün tanıtım metni var. İçeriği dikkate alarak tanıtıcı şekilde soruyu cevapla:

Context:
{context}

Soru: {question}
Cevap:"""
    else:
        return f"""Aşağıda bir belge içeriği var. Soruyu sadece içerikte geçen bilgilere göre açıkla. Uydurma, varsayım yapma:

Context:
{context}

Soru: {question}
Cevap:"""
