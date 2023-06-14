import logging
import asyncio
import aiohttp
import concurrent.futures
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tkinter import Tk
from tkinter import simpledialog
import webview
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required
from flask_caching import Cache
from flask_mail import Mail
import pandas as pd
import matplotlib.pyplot as plt


# Configure logging settings
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Application started.")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Replace with your desired database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your desired secret key

api = Api(app)
db = SQLAlchemy(app)
cache = Cache(app)
mail = Mail(app)


class CleanScraperBot:
    _instance = None
   
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.data = []
        self.logger = logging.getLogger("CleanScraperBot")

    def onUpdate(self, callback):
        self.update_callback = callback

    async def scrape_async(self, session, url, css_selector):
        async with session.get(url) as response:
            content_type = response.headers.get("content-type")
            if "text/xml" in content_type:
                xml_content = await response.text()
                self.parse_xml(xml_content)
            elif "application/json" in content_type:
                json_content = await response.json()
                self.parse_json(json_content)
            else:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                elements = soup.select(css_selector)
                for element in elements:
                    self.data.append(element.text)

        # Send real-time updates
        self.update_callback("Scraping in progress...")

    def run(self, urls_css_selectors):
        # Handle exceptions and send error messages
        try:
            # Run the scraping process
            asyncio.run(self._run_async(urls_css_selectors))

    def navigate(self, url):
        # Navigation logic goes here
        pass

    def run_gui(self):
        # GUI integration code goes here
        root = tk.Tk()
        root.title("CleanScraperBot")
        root.geometry("800x600")

        # Create the URL input field
        url_label = tk.Label(root, text="URL:")
        url_label.pack()
        url_entry = tk.Entry(root, width=80)
        url_entry.pack()

        # Create the CSS selector input field
        css_label = tk.Label(root, text="CSS Selector:")
        css_label.pack()
        css_entry = tk.Entry(root, width=80)
        css_entry.pack()

            # Perform scraping logic
            async with aiohttp.ClientSession() as session:
                tasks = []
                for url, css_selector in urls_css_selectors:
                    task = asyncio.ensure_future(self.scrape_async(session, url, css_selector))
                    tasks.append(task)
                await asyncio.gather(*tasks)
                
            # Process and analyze the scraped data
            self.clean_data()
            self.analyze_data()

            # Save the data to the database
            self.save_data()

        except Exception as e:
            self.logger.error(f"Error occurred: {str(e)}")
            raise e

    async def _run_async(self, urls_css_selectors):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url, css_selector in urls_css_selectors:
                task = asyncio.ensure_future(self.scrape_async(session, url, css_selector))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def clean_data(self):
        # Clean and preprocess the scraped data
        cleaned_data = []
        for item in self.data:
            clean_text = re.sub(r"[^a-zA-Z]", " ", item)
            clean_text = clean_text.lower()
            tokens = word_tokenize(clean_text)
            stop_words = set(stopwords.words("english"))
            tokens = [token for token in tokens if token not in stop_words]
            lemmatizer = WordNetLemmatizer()
            tokens = [lemmatizer.lemmatize(token) for token in tokens]
            tagged_tokens = pos_tag(tokens)
            nouns = [token for token, pos in tagged_tokens if pos.startswith("NN")]
            cleaned_data.append(" ".join(nouns))
        self.data = cleaned_data


    def parse_xml(self, xml_content):
        # XML parsing logic goes here
        pass

    def parse_json(self, json_content):
        # JSON parsing logic goes here
        pass


    def parse_excel(self, file_path):
        # Read and process student data from Excel sheets
        # ...

    def generate_graph(self, data):
        data = pd.read_excel(file_path)
        # Process the student data as per your requirements
        # Return the processed data Generate professional graphs based on the student data
        # ...

    def process_data_for_graph(self, data):
        # Preprocess the student data specifically for graph generation
        # ...

    def generate_graph(self, data):
        # Use matplotlib or other graphing libraries to create the desired graph
        # Customize the graph based on your requirements
        plt.plot(data['student_id'], data['score'], marker='o')
        plt.xlabel('Student ID')
        plt.ylabel('Score')
        plt.title('Student Performance')
        plt.grid(True)
        plt.show()



    def analyze_data(self):
    self.logger.debug("Analyzing data...")
    # Process the data and prepare it for graph generation
    student_data = self.process_data_for_graph()
    # Generate professional graphs
    self.generate_graph(student_data)


    def save_data(self):
        # Save the data to the database
        for item in self.data:
            data = Data(text=item)
            db.session.add(data)
        db.session.commit()

    
class ScrapedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"ScrapedData(id={self.id}, data={self.data})"



lass ScrapedDataResource(Resource):
    @jwt_required()
    def get(self):
        scraped_data = ScrapedData.query.all()
        return [{'id': item.id, 'data': item.data} for item in scraped_data]
    
    
    @jwt_required
    def post(self):
        data = request.get_json()
        urls_css_selectors = data['urls_css_selectors']

        bot = CleanScraperBot("/path/to/chromedriver")
        bot.run(urls_css_selectors)

        return {'message': 'Data scraped and saved successfully'}, 201


api.add_resource(ScrapedDataResource, '/data')


# Replace these dummy functions with your actual user authentication logic
def authenticate(username, password):
    if username == 'admin' and password == 'admin':
        return {'username': username}

def identity(payload):
    return payload['identity']

jwt = JWT(app, authenticate, identity)


@cache.cached(timeout=3600)  # Cache the result for 1 hour
def scrape_data():
    # Implement the logic for scraping data
    # ...
    return scraped_data

def close(self):
            # Clean up resources
        # ...

# Replace these dummy settings with your actual email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

@app.route('/send_email')
def send_email():
    # Implement the logic for sending an email
    # ...
    return 'Email sent successfully'



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    
    root = Tk()
    root.withdraw()

    urls_css_selectors = [
        ("http://example.com", ".css-selector-for-data"),
        # Add more URLs and CSS selectors here
    ]

    bot = CleanScraperBot("/path/to/chromedriver")
    bot.run(urls_css_selectors)

    webview.create_window("CleanScraperBot", "index.html", width=800, height=600)
    webview.start()
