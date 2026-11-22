#!/usr/bin/env python3
"""Прототип SEO-структуры «Для детских садов»: 6 подсайтов кабинетов + страницы материалов.
По ТЗ docs/tz/TZ_cabinet_subpages_seo_2026-11-22.md (ordo-ads). Запуск: python3 _tools/gen_cabinets.py"""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://aidabintazamat.github.io/ordo"
PLUS = "21 900 ₸/мес"
REG = "https://kz.ordo.education/#register-business"     # бесплатная регистрация сада (Free → 7 дней Plus)
LOGIN = "https://kz.ordo.education/"
from urllib.parse import quote
def WA(topic): return "https://wa.me/77767233070?text=" + quote(f"Здравствуйте! Хочу демо ORDO: {topic}")

CSS = """
@font-face{font-family:Manrope;src:url(BASE/assets/Manrope-500.ttf);font-weight:500}
@font-face{font-family:Manrope;src:url(BASE/assets/Manrope-700.ttf);font-weight:700}
@font-face{font-family:Manrope;src:url(BASE/assets/Manrope-800.ttf);font-weight:800}
:root{--t:#0E9C9C;--g:#8CB43C;--g2:#5C8A24;--gl:#EEF5E3;--tl:#E3F4F4;--ink:#1F2D3D;--mut:#5B6B7A;--line:#E1E8EE;--bg:#F1F4F7;--card:#fff}
*{box-sizing:border-box}body{margin:0;font-family:Manrope,system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.55;font-weight:500}
a{color:inherit;text-decoration:none}.wrap{max-width:1160px;margin:0 auto;padding:0 16px}
header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
.nav{display:flex;align-items:center;justify-content:space-between;height:64px;gap:12px}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:20px}.logo img{height:30px}
.nav nav{display:flex;gap:18px;font-size:15px;color:var(--mut);flex-wrap:wrap}.nav nav a:hover,.nav nav a.on{color:var(--t)}
.lang{font-size:14px;color:var(--mut)}.lang a{padding:4px 8px;border-radius:8px}.lang a.on{background:var(--tl);color:var(--t);font-weight:700}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:12px;background:var(--t);color:#fff;font-weight:700;border:0;cursor:pointer;font-size:15px}
.btn.g{background:var(--g)}.btn.ghost{background:#fff;color:var(--ink);border:1px solid var(--line)}
.crumbs{font-size:13px;color:var(--mut);padding:14px 0 0}.crumbs a{color:var(--t)}
.hero{padding:34px 0 26px}.hero h1{font-size:40px;line-height:1.12;margin:0 0 12px;letter-spacing:-.02em;max-width:860px}
.hero h1 em{font-style:normal;color:var(--t)}.lead{font-size:18px;color:var(--mut);max-width:720px;margin:0 0 22px}
section{padding:28px 0}h2{font-size:26px;margin:0 0 16px;letter-spacing:-.01em}h3{margin:0 0 6px;font-size:17px}
.grid{display:grid;gap:14px}.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 6px 22px rgba(31,45,61,.05)}
a.card:hover{border-color:var(--t)}.card p{margin:0;color:var(--mut);font-size:14px}
.ic{width:46px;height:46px;border-radius:13px;display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:10px}
.tag{display:inline-block;font-size:12px;background:var(--gl);color:var(--g2);padding:4px 10px;border-radius:999px;font-weight:700;margin:0 6px 6px 0}
.day{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;margin-bottom:12px}
.day h3{display:flex;justify-content:space-between;align-items:center}.day ol{margin:8px 0 0;padding-left:20px}.day li{margin:4px 0}
.day.lock{background:repeating-linear-gradient(135deg,#fff,#fff 14px,#F6F8FA 14px,#F6F8FA 28px);color:var(--mut)}
.day.lock h3 span{font-size:20px}.badge{font-size:12px;font-weight:700;padding:4px 10px;border-radius:999px;background:var(--gl);color:var(--g2)}
.plus{background:linear-gradient(135deg,var(--t),#0B7F86);color:#fff;border-radius:22px;padding:28px;display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap}
.plus p{color:#D8F1F1;margin:4px 0 0}.plus .btn{background:#fff;color:var(--t)}
details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 18px;margin-bottom:10px}summary{font-weight:700;cursor:pointer}
.chips a{display:inline-block;margin:0 8px 8px 0;padding:8px 14px;border-radius:999px;background:#fff;border:1px solid var(--line);font-size:14px}
.chips a.on,.chips a:hover{border-color:var(--t);color:var(--t)}
.note{font-size:13px;color:var(--mut);background:#FFF8E6;border:1px solid #F3E2B3;border-radius:12px;padding:10px 14px}
footer{padding:30px 0 90px;color:var(--mut);font-size:14px}
.hero .acts{display:flex;gap:10px;flex-wrap:wrap}.lockrow{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.lockrow small{color:var(--mut)}.mbar{display:none}
@media(max-width:820px){.mbar{display:flex;gap:8px;position:fixed;left:0;right:0;bottom:0;padding:10px 12px;background:#fff;border-top:1px solid var(--line);z-index:9}.mbar .btn{flex:1;justify-content:center;padding:12px 10px}.hdr-try{display:none}}
@media print{header,footer,.crumbs,.hero,.plus,details,section h2,.chips,.lock,.mbar,.noprint,.orbit{display:none!important}body{background:#fff}.day{border:0;box-shadow:none}}
/* орбита */
.orbit{position:relative;max-width:760px;aspect-ratio:1/1;margin:0 auto}
.orbit svg{position:absolute;inset:0;width:100%;height:100%}
.orbit .core{position:absolute;left:50%;top:50%;width:30%;aspect-ratio:1;transform:translate(-50%,-50%);background:#fff;border-radius:50%;box-shadow:0 18px 50px rgba(14,156,156,.25);display:flex;align-items:center;justify-content:center}
.orbit .core img{width:86%;animation:spin 14s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.orbit .node{position:absolute;transform:translate(-50%,-50%);background:#fff;border:1px solid var(--line);border-radius:16px;padding:10px 16px 10px 10px;display:flex;align-items:center;gap:10px;font-weight:700;box-shadow:0 10px 26px rgba(31,45,61,.08);white-space:nowrap;transition:.2s}
.orbit .node:hover{border-color:var(--t);box-shadow:0 0 0 4px var(--tl)}
.orbit .node .ic{width:40px;height:40px;margin:0;font-size:20px}
.ring{fill:none;stroke:var(--t);stroke-opacity:.45;stroke-width:3;stroke-dasharray:.1 9;stroke-linecap:round;transform-origin:50% 50%}
.r1{animation:spin 60s linear infinite}.r2{animation:spin 90s linear infinite reverse}
.ray{stroke:var(--g);stroke-width:3;stroke-dasharray:8 8;opacity:.9}
@media(max-width:820px){.g2,.g3{grid-template-columns:1fr}.hero h1{font-size:30px}.nav nav{display:none}
.orbit .node{padding:6px 10px 6px 6px;font-size:13px;gap:6px;border-radius:12px}.orbit .node .ic{width:28px;height:28px;font-size:15px;border-radius:8px}}
""".replace("BASE", BASE)

T = {
 "ru": {"for_parents": "Родителям", "for_gardens": "Для детских садов", "login": "Войти", "home": "Главная",
        "get_full": "Подключить Plus — 7 дней бесплатно", "trial": "7 дней бесплатно", "try": "Попробовать бесплатно", "demo": "💬 Демо в WhatsApp", "faq": "Частые вопросы",
        "other_cab": "Другие кабинеты", "materials": "Материалы кабинета", "open": "Открыто бесплатно",
        "locked": "Открыть — 7 дней бесплатно", "lock_hint": "Доступно в Plus", "proto": "Прототип структуры сайта для согласования. Тексты и материалы — демо."},
 "kk": {"for_parents": "Ата-аналарға", "for_gardens": "Балабақшаларға", "login": "Кіру", "home": "Басты бет",
        "get_full": "Plus қосу — 7 күн тегін", "trial": "7 күн тегін", "try": "Тегін байқап көру", "demo": "💬 WhatsApp-та демо", "faq": "Жиі қойылатын сұрақтар",
        "other_cab": "Басқа кабинеттер", "materials": "Кабинет материалдары", "open": "Тегін ашық",
        "locked": "Ашу — 7 күн тегін", "lock_hint": "Plus-та қолжетімді", "proto": "Сайт құрылымының прототипі. Мәтіндер — демо."},
}

AGES = [("rannii", "группы раннего возраста (1–2 года)", "ерте жас тобы (1–2 жас)"),
        ("mladshaya", "младшей группы (2–3 года)", "кіші топ (2–3 жас)"),
        ("srednyaya", "средней группы (3–4 года)", "ортаңғы топ (3–4 жас)"),
        ("starshaya", "старшей группы (4–5 лет)", "ересек топ (4–5 жас)"),
        ("predshkolnaya", "предшкольной группы (5–6 лет)", "мектепалды даярлық тобы (5–6 жас)")]

NOM = {"rannii": ("Ранняя группа", "Ерте жас тобы"), "mladshaya": ("Младшая группа", "Кіші топ"), "srednyaya": ("Средняя группа", "Ортаңғы топ"), "starshaya": ("Старшая группа", "Ересек топ"), "predshkolnaya": ("Предшкольная группа", "Мектепалды даярлық")}
DAYS_RU = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
DAYS_KK = ["Дүйсенбі", "Сейсенбі", "Сәрсенбі", "Бейсенбі", "Жұма"]
MON_RU = ["Утренний приём детей, беседа «Как я провёл выходные»", "Утренняя гимнастика (комплекс №1)",
          "Завтрак, дежурство по столовой", "Организованная деятельность: развитие речи — «Осенние листья»",
          "Организованная деятельность: физическая культура", "Прогулка: наблюдение за погодой, подвижная игра «Листопад»",
          "Обед, подготовка ко сну, дневной сон", "Гимнастика после сна, закаливание",
          "Самостоятельная игровая деятельность, работа с родителями"]
MON_KK = ["Балаларды қабылдау, «Демалыс күндерім» әңгімесі", "Таңертеңгі жаттығу (№1 кешен)",
          "Таңғы ас, асханадағы кезекшілік", "Ұйымдастырылған іс-әрекет: сөйлеуді дамыту — «Күзгі жапырақтар»",
          "Ұйымдастырылған іс-әрекет: дене шынықтыру", "Серуен: ауа райын бақылау, «Жапырақ түсу» қимылды ойыны",
          "Түскі ас, ұйқыға дайындық, күндізгі ұйқы", "Ұйқыдан кейінгі жаттығу, шынықтыру",
          "Өз бетімен ойын әрекеті, ата-аналармен жұмыс"]

# кабинеты: slug, name_ru, name_kk, emoji, color, lead_ru, функции, материалы [(slug, title_ru, desc, kind)]
CABS = [
 ("metodist", "Методический кабинет", "Әдістемелік кабинет", "📚", "#E7EEFF",
  "Для методиста и воспитателей: готовые циклограммы, конспекты, картотеки, сценарии и перспективные планы по Типовой учебной программе РК — на русском и казахском.",
  ["Готовая циклограмма на неделю для каждой группы", "Конспекты организованной деятельности", "Картотеки игр, прогулок и гимнастики",
   "Сценарии праздников RU + KK", "Перспективный план и карта развития ребёнка", "Воспитатель видит материалы только своей группы"],
  [("cyclogram", "Циклограмма", "по каждой группе на 2026–2027", "age"),
   ("konspekt", "Конспекты занятий / ОД", "ұйымдастырылған іс-әрекет, открытые занятия", "list"),
   ("kartoteka", "Картотеки", "игры, прогулки, гимнастика, сергіту сәті", "list"),
   ("scenariy", "Сценарии праздников", "алтын күз, жаңа жыл, 16 желтоқсан, выпускной", "list"),
   ("perspektivnyi-plan", "Перспективный план", "перспективалық / жылдық жоспар", "list"),
   ("karta-razvitiya", "Карта развития и мониторинг", "баланың жеке даму картасы", "list")]),
 ("hr", "Кабинет HR", "HR кабинеті", "👥", "#EEEAFB",
  "Для заведующей, директора, администратора и HR: табель посещаемости, должностные инструкции, штатное расписание, годовой план, лицензирование и госзаказ.",
  ["Электронный табель посещаемости с подписью", "Запись детей и учёт мест", "Должностные инструкции и штатное расписание",
   "Годовой план, педсоветы, номенклатура дел", "Чек-лист лицензирования и госзаказа", "Помощник воспитателя: чек-лист дня"],
  [("tabel", "Табель посещаемости", "электронный табель детского сада", "list"),
   ("dolzhnostnye-instrukcii", "Должностные инструкции", "воспитатель, помощник воспитателя, повар", "list"),
   ("shtatnoe-raspisanie", "Штатное расписание", "шаблон для детского сада", "list"),
   ("godovoi-plan", "Годовой план и педсовет", "заведующей детским садом", "list"),
   ("licenziya", "Лицензия и госзаказ", "как открыть детский сад, балабақша ашу", "list"),
   ("pomoshnik-vospitatelya", "Помощник воспитателя (няня)", "чек-лист дня, обязанности", "list")]),
 ("povar", "Кабинет повара", "Аспаз кабинеті", "🍲", "#FFF0E3",
  "Для повара и завхоза: меню детского сада по СанПиН, технологические карты блюд, бракеражные журналы и калькуляция питания.",
  ["10-дневное меню по СанПиН РК", "Технологические карты блюд для детского сада", "Бракеражный журнал готовой продукции",
   "Меню-раскладка и калькуляция", "Учёт продуктов на складе"],
  [("menu", "Меню детского сада", "10-дневное меню по СанПиН 2026", "list"),
   ("tehkarty", "Технологические карты блюд", "техкарты для детского сада", "list"),
   ("brakerazh", "Бракеражный журнал", "образец заполнения, скачать", "list")]),
 ("medik", "Медицинский кабинет", "Медициналық кабинет", "🩺", "#E2F5F3",
  "Для медсестры: журналы по новому СанПиН РК — бракераж сырой продукции, генеральная уборка, проветривание, мытьё игрушек, утренний фильтр, прививки.",
  ["Журналы по СанПиН в электронном виде", "Утренний фильтр и медосмотры", "План прививок (екпе журналы)",
   "Графики генуборки и проветривания", "Паспорт здоровья ребёнка"],
  [("sanpin", "СанПиН для детского сада", "59 бұйрық санпин балабақша", "list"),
   ("zhurnaly", "Журналы медсестры", "генуборка, проветривание, мытьё игрушек", "list"),
   ("utrennii-filtr", "Утренний фильтр", "журнал осмотра детей", "list"),
   ("privivki", "Прививки", "екпе журналы, денсаулық паспорты", "list")]),
 ("finansy", "Финансовый кабинет", "Қаржы кабинеті", "💰", "#FBF3DC",
  "Для бухгалтера и собственника: родительская оплата, долги, отчёты по каждой группе и саду.",
  ["Учёт родительской оплаты", "Напоминания о долгах", "Отчёты по группам и садам", "Касса и выгрузки"],
  [("roditelskaya-oplata", "Родительская оплата", "учёт оплат детского сада", "list")]),
 ("prodazhi", "Кабинет продаж", "Сату кабинеті", "🎯", "#FDE8E4",
  "Для менеджера по набору детей: CRM для детского сада — заявки, экскурсии, пробный день, договор.",
  ["Заявки из сайта, WhatsApp и Instagram в одной воронке", "Запись на экскурсию и пробный день", "Свободные места по возрасту", "Договор и оплата онлайн"],
  [("crm-dlya-detskogo-sada", "CRM для детского сада", "программа для набора детей", "list")]),
]
SHORT = {"metodist": ("Методический", "Әдістемелік"), "hr": ("HR", "HR"), "povar": ("Повар", "Аспаз"), "medik": ("Медик", "Медбике"), "finansy": ("Финансы", "Қаржы"), "prodazhi": ("Продажи", "Сату")}
CAB_KK_LEAD = {"metodist": "Әдіскер мен тәрбиешілерге: ҚР Үлгілік оқу бағдарламасы бойынша дайын циклограммалар, ұйымдастырылған іс-әрекет, картотекалар, сценарийлер — орыс және қазақ тілдерінде."}

def u(*parts, lang="ru"):
    p = "/".join(x.strip("/") for x in parts if x)
    pre = "kz/kk" if lang == "kk" else "kz"
    return f"{BASE}/{pre}/{p}/" if p else f"{BASE}/{pre}/"

def page(path, lang, title, desc, body, crumbs, alt=None, schema=None):
    t = T[lang]
    alt = alt or {}
    hre = "".join(f'<link rel="alternate" hreflang="{k}" href="{v}">' for k, v in alt.items())
    if alt: hre += f'<link rel="alternate" hreflang="x-default" href="{alt.get("ru-KZ", "")}">'
    canon = alt.get("ru-KZ" if lang == "ru" else "kk-KZ", "")
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": h} for i, (n, h) in enumerate(crumbs)]}
    sch = [bc] + (schema or [])
    crumbs_html = " › ".join(f'<a href="{h}">{html.escape(n)}</a>' for n, h in crumbs[:-1]) + (f" › {html.escape(crumbs[-1][0])}" if crumbs else "")
    lang_sw = ""
    if "kk-KZ" in alt:
        lang_sw = f'<span class="lang"><a class="{"on" if lang=="ru" else ""}" href="{alt.get("ru-KZ","#")}">RU</a><a class="{"on" if lang=="kk" else ""}" href="{alt.get("kk-KZ", alt.get("ru-KZ","#"))}">KK</a></span>'
    doc = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">{hre}
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<script type="application/ld+json">{json.dumps(sch, ensure_ascii=False)}</script>
<style>{CSS}</style></head><body>
<header><div class="wrap nav"><a class="logo" href="{BASE}/"><img src="{BASE}/assets/ordo-o.png" alt="ORDO">ORDO</a>
<nav><a href="{BASE}/">{t['for_parents']}</a><a class="on" href="{u('cabinets', lang=lang)}">{t['for_gardens']}</a></nav>
<span style="display:flex;gap:8px;align-items:center">{lang_sw}<a class="btn ghost" href="{LOGIN}">{t['login']}</a><a class="btn hdr-try" href="{REG}">{t['try']}</a></span></div></header>
<div class="wrap"><div class="crumbs">{crumbs_html}</div></div>
{body}
<footer><div class="wrap"><p class="note">{t['proto']}</p>© ORDO · ordo.education</div></footer>
<div class="mbar"><a class="btn" href="{REG}">{t['try']}</a><a class="btn ghost" href="{WA(title.split(' — ')[0].split(' | ')[0])}">💬 WhatsApp</a></div></body></html>"""
    out = ROOT / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return out

def plus_block(lang="ru", what="материалы"):
    t = T[lang]
    if lang == "kk":
        return f'<section><div class="wrap"><div class="plus"><div><h2 style="margin:0">Садик Plus — {PLUS}</h2><p>Барлық материалдар толық, жүктеу және басып шығару. {t["trial"]}.</p></div><a class="btn" href="{REG}">{t["get_full"]}</a></div></div></section>'
    return f'<section><div class="wrap"><div class="plus"><div><h2 style="margin:0">Садик Plus — {PLUS}</h2><p>Все {what} полностью, скачивание и печать. {t["trial"]}.</p></div><a class="btn" href="{REG}">{t["get_full"]}</a></div></div></section>'

def faq_block(qas, lang="ru"):
    sch = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}
    h = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in qas)
    return f'<section><div class="wrap"><h2>{T[lang]["faq"]}</h2>{h}</div></section>', sch

def other_cabs(cur, lang="ru"):
    items = "".join(f'<a class="card" href="{u("cabinets", c[0], lang=lang)}"><div class="ic" style="background:{c[4]}">{c[3]}</div><h3>{c[1] if lang=="ru" else c[2]}</h3></a>'
                    for c in CABS if c[0] != cur)
    return f'<section><div class="wrap"><h2>{T[lang]["other_cab"]}</h2><div class="grid g3">{items}</div></div></section>'

def orbit_html(lang="ru"):
    n = len(CABS); import math
    rays, nodes, dots = [], [], []
    for i, c in enumerate(CABS):
        a = math.radians(-60 + i * 60)
        x, y = 50 + 40 * math.cos(a), 50 + 40 * math.sin(a)
        ex, ey = 50 + 17 * math.cos(a), 50 + 17 * math.sin(a)
        rays.append(f'<line class="ray" x1="{x:.2f}" y1="{y:.2f}" x2="{ex:.2f}" y2="{ey:.2f}" vector-effect="non-scaling-stroke"/>')
        dots.append(f'<circle r="1.1" fill="#fff" stroke="#8CB43C" stroke-width="0.55"><animateMotion dur="2.4s" begin="-{i*0.4:.1f}s" repeatCount="indefinite" path="M{x:.2f},{y:.2f} L{ex:.2f},{ey:.2f}"/></circle>')
        name = SHORT[c[0]][0 if lang == "ru" else 1]
        nodes.append(f'<a class="node" style="left:{x:.2f}%;top:{y:.2f}%" href="{u("cabinets", c[0], lang=lang)}"><span class="ic" style="background:{c[4]}">{c[3]}</span>{name}</a>')
    return f"""<div class="orbit"><svg viewBox="0 0 100 100" aria-hidden="true">
<circle class="ring r1" cx="50" cy="50" r="24" vector-effect="non-scaling-stroke"/><circle class="ring r2" cx="50" cy="50" r="31" vector-effect="non-scaling-stroke"/><circle class="ring r1" cx="50" cy="50" r="38" vector-effect="non-scaling-stroke"/>
{''.join(rays)}{''.join(dots)}</svg>
<div class="core"><img src="{BASE}/assets/ordo-o.png" alt="ORDO"></div>{''.join(nodes)}</div>"""

def cyclo_embed(lang):
    """Блок «Циклограмма» прямо на главной странице методического кабинета (Аида TG 8106)."""
    t = T[lang]; days = DAYS_RU if lang == "ru" else DAYS_KK; mon = MON_RU if lang == "ru" else MON_KK
    chips = '<div class="chips">' + "".join(
        f'<a class="{"on" if a[0]=="srednyaya" else ""}" href="{u("cabinets","metodist","cyclogram",a[0],lang=lang)}">{NOM[a[0]][0 if lang=="ru" else 1]}</a>' for a in AGES) + "</div>"
    week = f'<div class="day"><h3>{days[0]} <span class="badge">{t["open"]}</span></h3><ol>' + "".join(f"<li>{html.escape(x)}</li>" for x in mon) + "</ol></div>"
    week += "".join(f'<div class="day lock"><div class="lockrow"><h3 style="margin:0">🔒 {d}</h3><span><small>{t["lock_hint"]}</small> <a class="btn ghost" href="{REG}">{t["locked"]}</a></span></div></div>' for d in days[1:])
    if lang == "ru":
        h = "Циклограмма на 2026–2027 — выберите группу"; sub = "Пример: средняя группа (3–4 года). Понедельник открыт, остальные дни — в кабинете с Plus. Воспитатель видит только свою группу."
        more = "Все циклограммы по группам →"
    else:
        h = "Циклограмма 2026–2027 — топты таңдаңыз"; sub = "Мысал: ортаңғы топ (3–4 жас). Дүйсенбі ашық, қалғаны — Plus."
        more = "Барлық топтардың циклограммасы →"
    return f'<section style="padding-top:0"><div class="wrap"><h2>🗓 {h}</h2><p class="lead" style="font-size:16px">{sub}</p>{chips}{week}<a class="btn" href="{u("cabinets","metodist","cyclogram",lang=lang)}">{more}</a></div></section>'

pages = []

# ---------- хаб «Для детских садов»
for lang in ("ru", "kk"):
    alt = {"ru-KZ": u("cabinets"), "kk-KZ": u("cabinets", lang="kk")}
    if lang == "ru":
        title = "Программа для детского сада — 6 кабинетов ORDO | CRM, табель, циклограмма"
        desc = "Программа для детского сада: методический кабинет, HR, повар, медик, финансы и продажи в одной системе. Готовые циклограммы, табель, меню, журналы СанПиН. 7 дней бесплатно."
        h1 = 'Весь детский сад <em>в одной системе</em>'
        lead = "6 кабинетов для всей команды сада: методика, HR, кухня, медицина, финансы и продажи. ORDO объединяет всех."
    else:
        title = "Балабақшаға арналған бағдарлама — ORDO 6 кабинеті"
        desc = "Балабақшаға арналған бағдарлама: әдістемелік кабинет, HR, аспаз, медбике, қаржы және сату бір жүйеде. Дайын циклограмма, табель, мәзір. 7 күн тегін."
        h1 = 'Бүкіл балабақша <em>бір жүйеде</em>'
        lead = "Бүкіл ұжымға арналған 6 кабинет: әдістеме, HR, ас үй, медицина, қаржы және сату."
    cards = "".join(f'<a class="card" href="{u("cabinets", c[0], lang=lang)}"><div class="ic" style="background:{c[4]}">{c[3]}</div><h3>{c[1] if lang=="ru" else c[2]}</h3><p>{c[5] if lang=="ru" else CAB_KK_LEAD.get(c[0], c[5])}</p></a>' for c in CABS)
    body = f"""<div class="hero"><div class="wrap"><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="acts"><a class="btn g" href="{REG}">{T[lang]['try']} — {T[lang]['trial']}</a><a class="btn ghost" href="{WA('ORDO')}">{T[lang]['demo']}</a></div></div></div>
<section style="padding-top:0"><div class="wrap">{orbit_html(lang)}</div></section>
<section><div class="wrap"><h2>{'Кабинеты' if lang=='ru' else 'Кабинеттер'}</h2><div class="grid g3">{cards}</div></div></section>"""
    qas = [("Что такое программа для детского сада ORDO?", "Онлайн-система с 6 кабинетами: методический (методист и воспитатели), HR (заведующая, директор, администратор, помощник воспитателя), повар, медик, финансы и продажи."),
           ("Сколько стоит?", f"Садик Plus — {PLUS}. Первые 7 дней бесплатно."),
           ("Есть ли казахский язык?", "Да, все кабинеты и материалы — на русском и казахском.")] if lang == "ru" else \
          [("ORDO бағдарламасы деген не?", "6 кабинеті бар онлайн-жүйе: әдістемелік, HR, аспаз, медбике, қаржы және сату."),
           ("Бағасы қанша?", f"Садик Plus — {PLUS}. Алғашқы 7 күн тегін.")]
    fb, fs = faq_block(qas, lang)
    body += plus_block(lang, "кабинеты") + fb
    path = "kz/kk/cabinets" if lang == "kk" else "kz/cabinets"
    crumbs = [(T[lang]["home"], BASE + "/"), (T[lang]["for_gardens"], u("cabinets", lang=lang))]
    pages.append(page(path, lang, title, desc, body, crumbs, alt,
                      [fs, {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "ORDO", "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                            "offers": {"@type": "Offer", "price": "21900", "priceCurrency": "KZT"}}]))

# ---------- подсайты кабинетов
for c in CABS:
    slug, name, name_kk, emo, col, lead, feats, mats = c
    fl = "".join(f'<div class="card"><h3>✓ {html.escape(f)}</h3></div>' for f in feats)
    ml = "".join(f'<a class="card" href="{u("cabinets", slug, m[0])}"><h3>{m[1]}</h3><p>{m[2]}</p></a>' for m in mats)
    body = f"""<div class="hero"><div class="wrap"><div class="ic" style="background:{col}">{emo}</div><h1>{name} <em>ORDO</em></h1><p class="lead">{lead}</p>
<div class="acts"><a class="btn g" href="{REG}">{T['ru']['try']} — {T['ru']['trial']}</a><a class="btn ghost" href="{WA('ORDO')}">{T['ru']['demo']}</a></div></div></div>
{cyclo_embed("ru") if slug == "metodist" else ""}
<section><div class="wrap"><h2>Что делает кабинет</h2><div class="grid g3">{fl}</div></div></section>
<section><div class="wrap"><h2>{T['ru']['materials']}</h2><div class="grid g3">{ml}</div></div></section>"""
    fb, fs = faq_block([(f"Для кого {name.lower()}?", lead), ("Можно попробовать бесплатно?", "Да, 7 дней бесплатно; часть материалов открыта без регистрации.")])
    body += plus_block() + fb + other_cabs(slug)
    alt = {"ru-KZ": u("cabinets", slug)}
    if slug == "metodist": alt["kk-KZ"] = u("cabinets", slug, lang="kk")
    crumbs = [(T["ru"]["home"], BASE + "/"), (T["ru"]["for_gardens"], u("cabinets")), (name, u("cabinets", slug))]
    pages.append(page(f"kz/cabinets/{slug}", "ru", f"{name} детского сада онлайн — ORDO", f"{name} ORDO: {lead}"[:300], body, crumbs, alt, [fs]))

    # страницы материалов
    for m in mats:
        mslug, mtitle, mdesc, kind = m
        mcrumbs = crumbs + [(mtitle, u("cabinets", slug, mslug))]
        if kind == "age":
            continue  # циклограмма — ниже отдельно
        items = [f"{mtitle}: материал {i}" for i in range(1, 7)]
        lst = f'<div class="day"><h3>{items[0]} <span class="badge">{T["ru"]["open"]}</span></h3><p>Демо-фрагмент открытого материала: текст виден на странице и доступен для поиска.</p><p style="margin-top:10px"><button class="btn ghost noprint" onclick="window.print()">🖨 Распечатать / сохранить PDF</button></p></div>'
        lst += "".join(f'<div class="day lock"><div class="lockrow"><h3 style="margin:0">🔒 {x}</h3><span><small>{T["ru"]["lock_hint"]}</small> <a class="btn ghost" href="{REG}">{T["ru"]["locked"]}</a></span></div></div>' for x in items[1:])
        body = f"""<div class="hero"><div class="wrap"><h1>{mtitle} <em>для детского сада</em></h1><p class="lead">{mdesc.capitalize()}. Готовые материалы ORDO по стандартам РК, на русском и казахском.</p></div></div>
<section style="padding-top:0"><div class="wrap">{lst}</div></section>"""
        fb, fs = faq_block([(f"Где скачать {mtitle.lower()}?", "Один материал открыт бесплатно на этой странице, все остальные — в кабинете ORDO с Садик Plus."),
                            ("Есть на казахском?", "Да, материалы на русском и казахском.")])
        body += plus_block() + fb + other_cabs(slug)
        pages.append(page(f"kz/cabinets/{slug}/{mslug}", "ru", f"{mtitle} для детского сада — {mdesc} | ORDO",
                          f"{mtitle} для детского сада: {mdesc}. Образец открыт бесплатно, все материалы — в {name.lower()} ORDO.", body, mcrumbs,
                          {"ru-KZ": u("cabinets", slug, mslug)}, [fs]))

# ---------- методический кабинет KK (главная подсайта)
c = CABS[0]
ml = "".join(f'<a class="card" href="{u("cabinets", "metodist", m[0], lang="kk") if m[0]=="cyclogram" else u("cabinets","metodist",m[0])}"><h3>{m[1]}</h3><p>{m[2]}</p></a>' for m in c[7])
body = f"""<div class="hero"><div class="wrap"><div class="ic" style="background:{c[4]}">{c[3]}</div><h1>{c[2]} <em>ORDO</em></h1><p class="lead">{CAB_KK_LEAD['metodist']}</p>
<div class="acts"><a class="btn g" href="{REG}">{T['kk']['try']} — {T['kk']['trial']}</a><a class="btn ghost" href="{WA('ORDO')}">{T['kk']['demo']}</a></div></div></div>
{cyclo_embed("kk")}
<section><div class="wrap"><h2>{T['kk']['materials']}</h2><div class="grid g3">{ml}</div></div></section>""" + plus_block("kk") + other_cabs("metodist", "kk")
pages.append(page("kz/kk/cabinets/metodist", "kk", "Балабақшаның әдістемелік кабинеті онлайн — ORDO", CAB_KK_LEAD["metodist"], body,
                  [(T["kk"]["home"], BASE + "/"), (T["kk"]["for_gardens"], u("cabinets", lang="kk")), (c[2], u("cabinets", "metodist", lang="kk"))],
                  {"ru-KZ": u("cabinets", "metodist"), "kk-KZ": u("cabinets", "metodist", lang="kk")}))

# ---------- циклограмма: хаб + 5 групп, RU и KK
def cyclo_week(lang):
    days = DAYS_RU if lang == "ru" else DAYS_KK
    mon = MON_RU if lang == "ru" else MON_KK
    t = T[lang]
    h = f'<div class="day"><h3>{days[0]} <span class="badge">{t["open"]}</span></h3><ol>' + "".join(f"<li>{html.escape(x)}</li>" for x in mon) + \
        f'</ol><p style="margin-top:10px"><button class="btn ghost noprint" onclick="window.print()">🖨 {"Распечатать / сохранить PDF" if lang=="ru" else "Басып шығару / PDF"}</button></p></div>'
    h += "".join(f'<div class="day lock"><div class="lockrow"><h3 style="margin:0">🔒 {d}</h3><span><small>{t["lock_hint"]}</small> <a class="btn ghost" href="{REG}">{t["locked"]}</a></span></div></div>' for d in days[1:])
    return h

for lang in ("ru", "kk"):
    t = T[lang]
    chips_all = lambda cur: '<div class="chips">' + "".join(
        f'<a class="{"on" if a[0]==cur else ""}" href="{u("cabinets","metodist","cyclogram",a[0],lang=lang)}">{NOM[a[0]][0 if lang=="ru" else 1]}</a>' for a in AGES) + "</div>"
    # хаб
    if lang == "ru":
        title = "Циклограмма в детском саду на 2026–2027 по приказу РК — все группы | ORDO"
        desc = "Готовая циклограмма для детского сада на 2026–2027 учебный год: ранняя, младшая, средняя, старшая и предшкольная группа. Понедельник открыт бесплатно, RU и KK."
        h1 = 'Циклограмма в детском саду <em>на 2026–2027</em>'
        lead = "Готовая циклограмма на неделю по Типовой учебной программе РК для каждой группы. Выберите группу — понедельник открыт бесплатно."
        qas = [("Что такое циклограмма в детском саду?", "Это план дня и недели группы: режимные моменты, организованная деятельность, прогулки и работа с родителями."),
               ("Есть циклограмма для разновозрастной группы?", "Да, в методическом кабинете ORDO есть циклограммы для всех групп, включая разновозрастные."),
               ("Можно скачать циклограмму бесплатно?", "Понедельник любой группы открыт бесплатно; вся неделя и год — с Садик Plus."),
               ("Есть циклограмма на казахском?", "Да: кіші топ, ортаңғы топ, ересек топ, мектепалды даярлық — на казахском языке.")]
    else:
        title = "Балабақшаға арналған циклограмма 2026–2027 — барлық топтар | ORDO"
        desc = "2026–2027 оқу жылына дайын циклограмма: ерте жас, кіші топ, ортаңғы топ, ересек топ, мектепалды даярлық. Дүйсенбі тегін ашық."
        h1 = 'Балабақшаға арналған циклограмма <em>2026–2027</em>'
        lead = "ҚР Үлгілік оқу бағдарламасы бойынша әр топқа апталық дайын циклограмма. Топты таңдаңыз — дүйсенбі тегін."
        qas = [("Циклограмма деген не?", "Топтың күндік және апталық жоспары: режим сәттері, ұйымдастырылған іс-әрекет, серуен."),
               ("Тегін жүктеуге бола ма?", "Әр топтың дүйсенбісі тегін; толық апта — Садик Plus арқылы.")]
    fb, fs = faq_block(qas, lang)
    grid = "".join(f'<a class="card" href="{u("cabinets","metodist","cyclogram",a[0],lang=lang)}"><h3>{"Циклограмма " + a[1] if lang=="ru" else a[2] + " циклограммасы"}</h3><p>{"понедельник открыт" if lang=="ru" else "дүйсенбі ашық"}</p></a>' for a in AGES)
    body = f"""<div class="hero"><div class="wrap"><h1>{h1}</h1><p class="lead">{lead}</p>{chips_all('')}</div></div>
<section style="padding-top:0"><div class="wrap"><div class="grid g3">{grid}</div></div></section>""" + plus_block(lang, "циклограммы") + fb + other_cabs("metodist", lang)
    base_path = "kz/kk/cabinets/metodist/cyclogram" if lang == "kk" else "kz/cabinets/metodist/cyclogram"
    cab_name = CABS[0][1] if lang == "ru" else CABS[0][2]
    crumbs = [(t["home"], BASE + "/"), (t["for_gardens"], u("cabinets", lang=lang)), (cab_name, u("cabinets", "metodist", lang=lang)),
              ("Циклограмма", u("cabinets", "metodist", "cyclogram", lang=lang))]
    alt = {"ru-KZ": u("cabinets", "metodist", "cyclogram"), "kk-KZ": u("cabinets", "metodist", "cyclogram", lang="kk")}
    pages.append(page(base_path, lang, title, desc, body, crumbs, alt, [fs]))
    # группы
    for a in AGES:
        g = a[1] if lang == "ru" else a[2]
        if lang == "ru":
            title = f"Циклограмма {g} на 2026–2027 по приказу РК | ORDO"
            desc = f"Готовая циклограмма {g} на неделю, 2026–2027 учебный год, Казахстан. Понедельник открыт бесплатно, вся неделя — в методическом кабинете ORDO."
            h1 = f'Циклограмма {g.split(" (")[0]} <em>на 2026–2027</em>'
            lead = f"Неделя {g}: режимные моменты, организованная деятельность, прогулки, работа с родителями. Воспитатель в кабинете видит циклограмму только своей группы."
        else:
            title = f"{g} циклограммасы 2026–2027 | ORDO"
            desc = f"{g} үшін дайын апталық циклограмма, 2026–2027 оқу жылы. Дүйсенбі тегін ашық."
            h1 = f'{g.split(" (")[0].capitalize()} циклограммасы <em>2026–2027</em>'
            lead = "Апта: режим сәттері, ұйымдастырылған іс-әрекет, серуен, ата-аналармен жұмыс."
        fb, fs = faq_block(qas[:2], lang)
        body = f"""<div class="hero"><div class="wrap"><h1>{h1}</h1><p class="lead">{lead}</p>{chips_all(a[0])}</div></div>
<section style="padding-top:0"><div class="wrap">{cyclo_week(lang)}</div></section>""" + plus_block(lang, "дни недели и вся программа года") + fb
        alt = {"ru-KZ": u("cabinets", "metodist", "cyclogram", a[0]), "kk-KZ": u("cabinets", "metodist", "cyclogram", a[0], lang="kk")}
        pages.append(page(f"{base_path}/{a[0]}", lang, title, desc, body, crumbs + [(NOM[a[0]][0 if lang=="ru" else 1], alt["ru-KZ" if lang=="ru" else "kk-KZ"])], alt, [fs]))

# ---------- sitemap (дополняем)
sm = ROOT / "sitemap.xml"
urls = sorted({BASE + "/" + str(p.parent.relative_to(ROOT)) + "/" for p in pages})
old = sm.read_text(encoding="utf-8") if sm.exists() else '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n'
add = "".join(f"<url><loc>{x}</loc></url>\n" for x in urls if x not in old)
sm.write_text(old.replace("</urlset>", add + "</urlset>"), encoding="utf-8")
print(len(pages), "pages")
