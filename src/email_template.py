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
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" style="width: 100%; border-collapse: collapse;">
        <tr>
            <td align="center" style="padding: 40px 0;">
                <table role="presentation" style="width: 600px; max-width: 100%; border-collapse: collapse; background-color: #ffffff; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-radius: 8px; overflow: hidden;">
                    
                    <!-- Header -->
                    <tr>
                        <td style="padding: 40px 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); text-align: center;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700;">🤖 AI Insight Daily</h1>
                            <p style="margin: 10px 0 0 0; color: #e0e7ff; font-size: 16px;">5 Concepts, 5 Minutes</p>
                        </td>
                    </tr>
                    
                    <!-- Date Bar -->
                    <tr>
                        <td style="padding: 20px 30px; background-color: #f8f9fa; border-bottom: 3px solid #667eea;">
                            <p style="margin: 0; color: #6b7280; font-size: 14px; text-align: center;">📅 {date}</p>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px; color: #1f2937;">
                            <p style="margin: 0 0 20px 0; color: #374151; font-size: 17px;">Hello AI Learner! 👋</p>
                            <p style="margin: 0 0 30px 0; color: #6b7280; font-size: 15px;">Here are your 5 new AI concepts for today. Let's expand your knowledge!</p>
                            
                            <div style="line-height: 1.8;">
                                {html_content}
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="padding: 30px; background-color: #1f2937; text-align: center;">
                            <p style="margin: 0 0 10px 0; color: #9ca3af; font-size: 14px;">Keep learning, keep growing! 🚀</p>
                            <p style="margin: 0; color: #6b7280; font-size: 12px;">AI Insight Daily - Your Daily Dose of AI Knowledge</p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
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
        html_lines = []
        in_list = False
        
        for line in lines:
            line = line.strip()
            
            if not line:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append('<br>')
                continue
            
            # Headings
            if line.startswith('###'):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                heading = line.replace('###', '').strip()
                html_lines.append(f'<h3 style="color: #667eea; margin: 25px 0 15px 0; font-size: 20px;">{heading}</h3>')
            elif line.startswith('##'):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                heading = line.replace('##', '').strip()
                html_lines.append(f'<h2 style="color: #667eea; margin: 30px 0 15px 0; font-size: 22px;">{heading}</h2>')
            elif line.startswith('#'):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                heading = line.replace('#', '').strip()
                html_lines.append(f'<h2 style="color: #667eea; margin: 30px 0 15px 0; font-size: 22px; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">{heading}</h2>')
            # Bullet points
            elif line.startswith('-') or line.startswith('•') or line.startswith('*'):
                if not in_list:
                    html_lines.append('<ul style="margin: 10px 0; padding-left: 20px;">')
                    in_list = True
                item = line[1:].strip()
                html_lines.append(f'<li style="margin: 8px 0; color: #374151; font-size: 15px;">{item}</li>')
            # Bold text
            elif line.startswith('**') and line.endswith('**'):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                bold_text = line.replace('**', '').strip()
                html_lines.append(f'<p style="margin: 15px 0; color: #1f2937; font-weight: 600; font-size: 16px;">{bold_text}</p>')
            # Regular paragraph
            else:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                # Handle inline bold (replace pairs of **)
                formatted_line = line
                while '**' in formatted_line:
                    formatted_line = formatted_line.replace('**', '<strong>', 1).replace('**', '</strong>', 1)
                html_lines.append(f'<p style="margin: 12px 0; color: #4b5563; font-size: 15px; line-height: 1.6;">{formatted_line}</p>')
        
        if in_list:
            html_lines.append('</ul>')
        
        return '\n'.join(html_lines)
