# Inferencia del clasificador de SMS (Proyecto 8, Corte 3)
from pathlib import Path
import joblib

_RUTA = Path(__file__).resolve().parent.parent / "models" / "modelo_final_sms.joblib"
_PAQ = None

def _cargar():
    global _PAQ
    if _PAQ is None:
        _PAQ = joblib.load(_RUTA)
    return _PAQ

def clasificar_sms(texto, umbral=None):
    # Devuelve etiqueta (ham/spam), probabilidad de spam y el umbral usado
    paq = _cargar()
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("El mensaje debe ser un texto no vacío.")
    t = paq["umbral"] if umbral is None else float(umbral)
    modelo = paq["modelo"]
    p = float(modelo.predict_proba([texto])[0][list(modelo.classes_).index("spam")])
    return {"mensaje": texto, "etiqueta": "spam" if p >= t else "ham",
            "prob_spam": round(p, 4), "umbral": t,
            "aviso": "Modelo entrenado con SMS en inglés (2000-2004). No validado en otros idiomas."}

if __name__ == "__main__":
    import sys
    for m in (sys.argv[1:] or ["Hey, are we still meeting for lunch today?"]):
        print(clasificar_sms(m))
