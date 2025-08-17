from flask import Flask, render_template_string
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# HTML template with embedded CSS and JavaScript
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>rafa felix, phd</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 3rem;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 90%;
            animation: fadeInUp 0.8s ease-out;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 300;
            margin-bottom: 0.5rem;
            color: #2d3748;
            letter-spacing: -0.5px;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #718096;
            margin-bottom: 2rem;
            font-weight: 400;
        }

        .description {
            font-size: 1.1rem;
            color: #4a5568;
            margin-bottom: 2.5rem;
            line-height: 1.7;
        }

        .nav-links {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .nav-link {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }

        .nav-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 2rem;
        }

        .social-link {
            display: inline-block;
            width: 40px;
            height: 40px;
            background: #f7fafc;
            border: 2px solid #e2e8f0;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #718096;
            text-decoration: none;
            transition: all 0.3s ease;
        }

        .social-link:hover {
            background: #667eea;
            border-color: #667eea;
            color: white;
            transform: scale(1.1);
        }

        .footer {
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid #e2e8f0;
            color: #a0aec0;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .container {
                padding: 2rem;
                margin: 1rem;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .nav-links {
                flex-direction: column;
                align-items: center;
            }
            
            .nav-link {
                width: 100%;
                max-width: 250px;
            }
        }

        .floating-elements {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .floating-element {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }

        .floating-element:nth-child(1) {
            width: 80px;
            height: 80px;
            top: 20%;
            left: 10%;
            animation-delay: 0s;
        }

        .floating-element:nth-child(2) {
            width: 120px;
            height: 120px;
            top: 60%;
            right: 15%;
            animation-delay: 2s;
        }

        .floating-element:nth-child(3) {
            width: 60px;
            height: 60px;
            bottom: 20%;
            left: 20%;
            animation-delay: 4s;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }
    </style>
</head>
<body>
    <div class="floating-elements">
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
    </div>
    
    <div class="container">
        <h1>rafa felix, phd</h1>
        <div class="subtitle">comp. scientist, climber, cyclist</div>
        
        <div class="description">
            Welcome to my personal space. I'm passionate about computer science, 
            outdoor adventures, and pushing boundaries both in technology and nature.
        </div>
        
        <div class="nav-links">
            <a href="#" class="nav-link">About</a>
            <a href="#" class="nav-link">Projects</a>
            <a href="#" class="nav-link">Publications</a>
            <a href="#" class="nav-link">Résumé</a>
        </div>
        
        <div class="social-links">
            <a href="#" class="social-link" title="GitHub">📚</a>
            <a href="#" class="social-link" title="LinkedIn">💼</a>
            <a href="#" class="social-link" title="Twitter">🐦</a>
            <a href="#" class="social-link" title="Email">✉️</a>
        </div>
        
        <div class="footer">
            rafa felix, phd © 2024
        </div>
    </div>

    <script>
        // Add some interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            const container = document.querySelector('.container');
            const navLinks = document.querySelectorAll('.nav-link');
            
            // Add hover effect to container
            container.addEventListener('mouseenter', function() {
                this.style.transform = 'scale(1.02)';
            });
            
            container.addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1)';
            });
            
            // Add click effect to nav links
            navLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    this.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        this.style.transform = 'scale(1)';
                    }, 150);
                });
            });
        });
    </script>
</body>
</html>
'''

@app.route("/")
def index():
    return HTML_TEMPLATE

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is the about page.</p>"

@app.route("/projects")
def projects():
    return "<h1>Projects Page</h1><p>This is the projects page.</p>"

@app.route("/publications")
def publications():
    return "<h1>Publications Page</h1><p>This is the publications page.</p>"

@app.route("/resume")
def resume():
    return "<h1>Résumé Page</h1><p>This is the résumé page.</p>"

if __name__ == "__main__":
    
    port_env = int(os.environ.get("PORT", 8080))
    debug_env = int(os.environ.get("DEBUG", False))

    app.run(host="0.0.0.0", port=port_env, debug=debug_env)
