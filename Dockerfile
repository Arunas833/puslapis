# Naudojame oficialų Python 3.10 variantą, kuris yra mažesnis
FROM python:3.10-slim

# Nustatome darbo katalogą konteineryje
WORKDIR /app

# Kopijuojame priklausomybių sąrašą į konteinerį
COPY requirements.txt /app/

# Atnaujiname pip ir įdiegiame priklausomybes
RUN pip install --upgrade pip && pip install -r requirements.txt

# Kopijuojame visus projekto failus į konteinerį
COPY . /app/

# Atidengiame 8000 portą (galima palikti informaciniais tikslais)
EXPOSE 8000

# Nurodome, kad naudosime PORT kintamąjį, kurį Railway nustato automatiškai
ENV PORT=8000

# Paleidžiame Django serverį su nurodytu portu
CMD ["python", "manage.py", "runserver", "0.0.0.0:${PORT}"]
