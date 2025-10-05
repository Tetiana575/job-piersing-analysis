import csv
import pandas as pd
from datetime import datetime
import tempfile
import os

# Читаем обработанный файл   
df = pd.read_csv('parsing_personalsachbearbeiter.csv', encoding='utf-8')

# Удаляем дубликаты по всей строке
df = df.drop_duplicates()

# Удаляем строки, содержащие стопслова в 'title'
stopwords = ['Ausbildung', 'Studium', 'Duales', 'Weiterbildung', 'Werkstudent', 'Student', 'Studentische','Auszubildener', 'Ausbildener','Auszubildende','SAP', 'Einkauf', 'Recruting', 'Manager', 'Kaufmanischer']
mask = df['title'].str.lower().apply(lambda x: not any(word.lower() in str(x) for word in stopwords))
df= df[mask]

#заменяет часть текста в столбце url, чтоб можно было посмотреть объявлние
# Обработка столбца 'url'
df['url'] = df['url'].apply(lambda x: x.replace('/stellenangebote', 'https://www.stepstone.de/jobs') if pd.notnull(x) else x)


# Обработка даты: преобразование из формата 2025-08-21T08:56:13+02:00 в формат 2025-08-25
def convert_date(date_str):
    # Парсим дату с учетом таймзоны
    dt = datetime.fromisoformat(date_str)
    # Можно оставить только дату (год-месяц-день)
    return dt.strftime('%Y-%m-%d')

df['datePosted'] = df['datePosted'].apply(convert_date)

# Обработка для поиска ключевых слов в Arbetszeit
keywords_employment = ['Vollzeit', 'Teilzeit',  'Minijob', 'Schicht', 'Nacht', 'Wochenende', 'Minijob']  # пример ключевых слов

def find_employment(text):
    if pd.isnull(text):
        return []
    found_keywords = [word for word in keywords_employment if word.lower() in text.lower()]
    return found_keywords
df['Arbetszeit'] = df['textSnippet'].apply(find_employment)

# Обработка для поиска ключевых слов в Arbeitsbedingungen
keywords_arbeitsbedingungen = ['Arbeitnehmerüberlassung', 'Zeitarbeit','Festanstellung']

def find_arbeitsbedingungen(text):
    if pd.isnull(text):
        return []
    found_keywords = [word for word in keywords_arbeitsbedingungen if word.lower() in text.lower()]
    return found_keywords
df['Arbeitsbedingungen'] = df['textSnippet'].apply(find_arbeitsbedingungen)

#Обработка для поиска ключевых слов в softskils
Softskils = ['Kommunikationsfähigkeit', 
 'Organisationstalent',
 'Problemlösungsfähigkeit',
 'Belastbarkeit', 'Diskretion',  
 'Vertrauenswürdigkeit',
'Empathie', 
'soziale Kompetenz',
'Flexibilität',
'Anpassungsfähigkeit',
'Selbstständiges',
'Selbstständigkeit',
'Konfliktfähigkeit',
'Verantwortungsbewusstsein',
'Lernbereitschaft',
'Zuverlässigkeit',
'Genauigkeit',
'Kommunikationsstärke',
'Teamfähigkeit',
'Dienstleistungsorientierung',
'Lösungsorientierung',
'Zeitmanagement',
'Stressresistenz',
'Teamarbeit', 
'Zusammenarbeit',
'Kollaboration',
'Kollaborationsfähigkeit']
def find_Softskils(text):
    if pd.isnull(text):
        return []
    softskils_keywords = [word for word in Softskils if word.lower() in text.lower()]
    return softskils_keywords
df['Softskils'] = df['textSnippet'].apply(find_Softskils)

#Обработка для поиска ключевых слов в hardskils
hardskils = [ 'Arbeitsrechts', 'Arbeitsvertragsrecht', 'Kündigungsschutzrecht', 'Arbeitszeitgesetzes', 'ArbZG', 'Entgeltabrechnung',
'Mutterschutzrecht', 'Elterngeldrecht',
'Gleichbehandlungsgesetz', 'AGG',
'Tarifvertragsrecht',
'DSGVO', 'Präsentationen ',
'HR-Software', 'SAP', 'datev', 'HR-System', 'HCM', 'Paisy', 'MS Ofice', 'Exel', 'Word'
'Organisationsfähigkeit', 'Dokumentenmanagement' ]

def find_hardskils(text):
    if pd.isnull(text):
        return []
    hardskils_keywords = [word for word in hardskils if word.lower() in text.lower()]
    return hardskils_keywords
df['Hardskils'] = df['textSnippet'].apply(find_hardskils)

verantwortlichkeiten = ['Abwicklung','administrativen Aufgaben','Personalprozesse bearbeiten','Personalwesen',
'Elternzeit verwalten',
'Arbeitszeitmanagement',
'Versetzungen koordinieren',
'Austritte bearbeiten',
'Personalvorgängen',
'HR-Systeme', 
'Human Resources Systeme',
'Arbeitsverträge', 
'Zusatzvereinbarungen',
'Zeugnisse',
'Koordination',
'Verfolgung' ,
'Beratung',
'Betreuung' 
'Finanzbereich',
'Einrichtungen betreuen',
'Kirchengemeinden unterstützen',
'Zeitwirtschaft',
'Personalbetreuung',
'HR-Kenntnisse',
'Ansprechperson', 
'Arbeitsverhältnis',
'Arbeitszeit',
'Abwesenheitszeiten',
'Zeitwirtschaftssystem',
'Förderung Mitglieder/KundInnen'
'Unterstützung',
'Personalbetreuung',
'Lohnabrechnung', 
'Gehaltsabrechnung',
'Zeiterfassung',
'Recruiting',
'Onboarding',
'Offboarding',
'Vertragsmanagement',
'Lohnsteuerprüfungen', 
'Sozialversicherungsprüfungen',
'Projektmitwirkung',
'Optimierung' 
]

def find_verantwortlichkeiten(text):
    if pd.isnull(text):
        return []
    verantwortlichkeiten_keywords = [word for word in verantwortlichkeiten if word.lower() in text.lower()]
    return verantwortlichkeiten_keywords

# Применение функции к колонке 'textSnippet' и сохранение результата в новую колонку как список списков
df['verantwortlichkeiten'] = df['textSnippet'].apply(find_verantwortlichkeiten)

#Обработка для поиска ключевых слов в sprache
sprache = ['Englisch', 'Französisch', 'Spanisch', 'Italienisch', 'Portugiesisch', 'Russisch', 'Deutsch']

def find_sprache(text):
    if pd.isnull(text):
        return []
    sprache_keywords = [word for word in sprache if word.lower() in text.lower()]
    return sprache_keywords
df['sprache'] = df['textSnippet'].apply(find_sprache)

#Обработка для поиска ключевых слов в branche
branche = ['Systemtechnik ','Gesundheit', 'Soziales', 'Metall', 'Maschinenbau', 'Anlagenbau', 'Einzelhandel','Flugzeug' 
'Großhandel', 'Außenhandel', 'Bau', 'Architektur','Öffentlicher Dienst', 'Organisationen', 'Logistik', 'Transport', 'Verkehr', 
 'Telekommunikation', 'Sicherheitsdienstleistungen', 'Reinigungsdienstleistungen', 'Reparaturdienstleistungen', 'Hotel',
 'Gaststätten', 'Tourismus', 'Bank', 'Banken', 'Finanzdienstleistungen', 'Immobilien', 'Versicherungen', 
'Elektro', 'Feinmechanik', 'Optik', 'Medizintechnik', 'Sonstige Dienstleistungen', 'Nahrungsmittelherstellung', 
'Genussmittelherstellung', 'Erziehung', 'Unterricht', 'Rohstoffverarbeitung', 'Glas', 'Keramik', 'Kunststoff', 'Holz',
'Chemie', 'Pharma', 'Biotechnologie', 'Fahrzeugbau', 'Fahrzeuginstandhaltung', 'Abfallwirtschaft', 'Energieversorgung', 
'Wasserversorgung', 'Wissenschaft', 'Forschung',  'Arbeitsvermittlung', 'privat',
'Papier', 'Druck', 'Verpackung', 'Konsumgüter', 'Gebrauchsgüter', 'Landwirtschaft', 'Forstwirtschaft', 'Gartenbau', 
'Rohstoffgewinnung', 'Rohstoffaufbereitung', 'Medien', 'Informationsdienste',  'Öffentlichkeitsarbeit']

def find_branche(text):
    if pd.isnull(text):
        return []
    branche_keywords = [word for word in branche if  word.lower() in text.lower()]
    return branche_keywords
df['branche'] = df['textSnippet'].apply(find_branche)

#Обработка для поиска ключевых слов в greed
keywords_greed = ['Junior', 'Middle', 'Senior', 'Leiter', 'Practikant', 'Teamleitung', 'Teamleiter', 'Teammitglied', 'Spezialist', 'Specialist', 'Experte', 'Expert', 'Intern']  # пример ключевых слов
def find_greed(text):
    if pd.isnull(text):
        return []
    found_keywords = [word for word in keywords_greed if word.lower() in text.lower()]
    return found_keywords
df['Greed'] = df['title'].apply(find_greed)

#создаем столбец 'home_work' и заполняем его значениями
# Создаем новый столбец 'home_work' с условной логикой
df['home_work'] = df['workFromHome'].apply(
    lambda x: ['Home Work'] if x == 2 else (['Ofice Work'] if x == 0 else None)
)

#Отбор нужных колонок и сохранение в новый CSV
df1 = df[['id', 'url', 'title', 'companyName',  'datePosted', 'location', 'salary', 'workFromHome',  'Arbetszeit', 'Softskils', 'Hardskils', 'Arbeitsbedingungen', 'branche', 'verantwortlichkeiten','sprache', 'Greed','home_work','textSnippet']]
df1.to_csv('personalsachbearbeiter.csv', index=False, encoding='utf-8')