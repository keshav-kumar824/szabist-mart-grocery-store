# SZABIST MART - Online Grocery Store

A modern web-based grocery store built with Flask and TailwindCSS, containerized with Docker.

## Features
- Browse products by category
- Search functionality
- Product detail pages
- Admin stock management
- Responsive design

## Technologies Used
- **Backend**: Python Flask
- **Frontend**: HTML, TailwindCSS, JavaScript
- **Data**: JSON
- **Containerization**: Docker & Docker Compose

## Prompt Provided to AI:
Enhance the UI of a Flask-based grocery store website using Tailwind CSS. Do not modify any Flask code, Python logic, or JSON data. The enhancements should include:

* A hero section on the home page with grocery-themed images and a call-to-action.

*** A navbar with links to Home, Products, About, and Contact.
* There should be 4 pages A home page , A product page , A contact and about page(together) , And a product detail page .**

* the html codes should be only 4 files

* Each page should be responsive along with it product page should have every functionality perfromed in main.py file like updating the item out of stock .

* A product listing page that displays each product from the JSON as a card, and each product should have images like if there is milk it should have image of milk , including image, name, category, price, and description.

* A responsive grid layout for product cards.

* A footer with social media links, contact info, and copyright.

* Smooth styling, spacing, colors, and hover effects using Tailwind CSS.

* Responsive design for mobile, tablet, and desktop.

* modify the main.py file just by replacing the book terms with products and insert all pages in main.py.

* remember there should be no change in python or flask file there logic should remain as it is.
* The website is powered by Flask and serves JSON data for products. The JSON structure contains 30 products with fields: `product\_id`, `name`, `category`, `price`, `quantity`, `image`, `description`. The website already has `index.html` and other templates. You must only enhance the HTML/CSS, not modify Python/JSON.

* Tailwind CSS best practices: https://tailwindcss.com/docs

* Example grocery layouts: hero section + product cards + navbar + footer

* Use CDN version of Tailwind CSS if local build is not available.
  
## Quick Start with Docker

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/szabist-mart.git
cd szabist-mart
```

2. Run with Docker Compose:
```bash
docker compose up --build
```

3. Open your browser: `http://localhost:5000`

## Manual Installation (Without Docker)

1. Navigate to app directory:
```bash
cd app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Project Structure
```
szabist-mart/
├── app/
│   ├── app.py
│   ├── products.json
│   ├── requirements.txt
│   ├── .gitignore
|   ├── .python-version
|   ├── pyproject.toml
|   ├── uv.lock
|   ├── templates/
│   └── static/
├── Dockerfile
├── compose.yml
└── README.md
```

## Created By
Ayush and Keshav


## License
MIT

# My Website

Welcome! Check out my project.

[Preview Website](https://szabist-mart-grocery-store--keshavlund62.replit.app)
