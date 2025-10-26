"""
Email Template module for creating beautiful HTML emails.
Generates responsive email layouts.
"""

from datetime import datetime
from typing import Optional


class EmailTemplate:
    """Class to generate beautiful HTML email templates"""
    
    @staticmethod
    def create_html_email(concepts_text: str, date: Optional[str] = None) -> str:
        """
        Create a beautiful, responsive HTML email template
        
        Args:
            concepts_text: The AI concepts content
            date: Date string (defaults to today)
            
        Returns:
            Complete HTML email string
        """
        if date is None:
            date = datetime.now().strftime("%B %d, %Y")
        
        # Convert plain text to HTML with proper formatting
        html_content = EmailTemplate._format_content(concepts_text)
        
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Insight Daily</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #f3f4f6;
            font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            color: #1f2937;
        }}
        .wrapper {{
            width: 100%;
            background: linear-gradient(135deg, #6b73ff 0%, #000dff 100%);
            padding: 40px 0;
        }}
        .container {{
            width: 600px;
            max-width: 90%;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 20px 45px rgba(15, 23, 42, 0.18);
        }}
        .header {{
            padding: 45px 35px 35px;
            text-align: center;
            background: radial-gradient(circle at top left, #a5b4fc, #4c1d95);
            color: #ffffff;
        }}
        .header h1 {{
            margin: 0 0 12px;
            font-size: 30px;
            letter-spacing: 0.6px;
        }}
        .header p {{
            margin: 0;
            font-size: 16px;
            color: rgba(255, 255, 255, 0.85);
        }}
        .date-bar {{
            padding: 14px 35px;
            background: #eef2ff;
            border-bottom: 1px solid #c7d2fe;
            text-align: center;
            font-size: 14px;
            color: #4338ca;
            font-weight: 600;
            letter-spacing: 0.4px;
        }}
        .content {{
            padding: 35px;
            background: linear-gradient(180deg, rgba(249, 250, 251, 0.94) 0%, #ffffff 45%);
        }}
        .intro {{
            margin: 0 0 28px;
            font-size: 17px;
            color: #334155;
            line-height: 1.6;
        }}
        .concept-card {{
            background: #ffffff;
            border-radius: 14px;
            padding: 22px 24px;
            margin-bottom: 18px;
            border: 1px solid rgba(99, 102, 241, 0.18);
            box-shadow: 0 15px 30px rgba(15, 23, 42, 0.08);
        }}
        .concept-card h3 {{
            margin: 0 0 14px;
            font-size: 20px;
            color: #312e81;
        }}
        .concept-card p {{
            margin: 12px 0;
            font-size: 15px;
            color: #475569;
            line-height: 1.6;
        }}
        .concept-card ul {{
            margin: 10px 0 0 18px;
            padding: 0;
        }}
        .concept-card li {{
            margin: 6px 0;
            color: #374151;
            font-size: 15px;
        }}
        .concept-card strong {{
            color: #1f2937;
        }}
        .footer {{
            padding: 32px 28px 36px;
            background: #0f172a;
            text-align: center;
            color: rgba(226, 232, 240, 0.85);
            font-size: 13px;
        }}
        .footer p {{
            margin: 6px 0;
        }}
        @media (max-width: 640px) {{
            .content {{
                padding: 24px;
            }}
            .concept-card {{
                padding: 20px;
            }}
            .concept-card h3 {{
                font-size: 18px;
            }}
        }}
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="container">
            <div class="header">
                <h1>🤖 AI Insight Daily</h1>
                <p>5 Concepts, 5 Minutes • Curated for Moussaab Boutelis</p>
            </div>
            <div class="date-bar">📅 {date}</div>
            <div class="content">
                <p class="intro">Hello Moussaab! 👋 Welcome to your daily briefing. Here are the five freshest AI concepts curated to expand your knowledge today.</p>
                {html_content}
            </div>
            <div class="footer">
                <p>Stay curious, keep building! 🚀</p>
                <p>AI Insight Daily • Moussaab Boutelis</p>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        return html_template
    
    @staticmethod
    def _format_content(content: str) -> str:
        """
        Format plain text content into HTML with proper styling
        
        Args:
            content: Plain text content
            
        Returns:
            Formatted HTML content
        """
        lines = content.split('\n')
        html_lines: list[str] = []
        in_list = False
        inside_card = False

        def close_list():
            nonlocal in_list
            if in_list:
                html_lines.append('</ul>')
                in_list = False

        def close_card():
            nonlocal inside_card
            if inside_card:
                close_list()
                html_lines.append('</div>')
                inside_card = False

        for raw_line in lines:
            line = raw_line.strip()

            if not line:
                close_list()
                continue

            is_heading = False
            heading_text = ''

            if line.startswith('#'):
                is_heading = True
                heading_text = line.lstrip('#').strip()
            elif line.startswith('**') and line.endswith('**'):
                heading_text = line.strip('* ')
                is_heading = len(heading_text.split()) <= 8
            elif line[0].isdigit() if line else False:
                is_heading = True
                heading_text = line

            if is_heading and heading_text:
                close_card()
                inside_card = True
                html_lines.append('<div class="concept-card">')
                html_lines.append(f'<h3>{heading_text}</h3>')
                continue

            if line.startswith(('-', '•', '*')):
                if not inside_card:
                    inside_card = True
                    html_lines.append('<div class="concept-card">')
                if not in_list:
                    html_lines.append('<ul>')
                    in_list = True
                html_lines.append(f'<li>{line[1:].strip()}</li>')
                continue

            close_list()

            if not inside_card:
                inside_card = True
                html_lines.append('<div class="concept-card">')

            formatted_line = line
            while '**' in formatted_line:
                formatted_line = formatted_line.replace('**', '<strong>', 1).replace('**', '</strong>', 1)
            html_lines.append(f'<p>{formatted_line}</p>')

        close_card()

        return '\n'.join(html_lines)
