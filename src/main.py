"""
Main module for AI Insight Daily project.
Orchestrates the daily email generation and sending workflow.
"""

import sys
from config import config
from storage import ConceptStorage
from ai_generator import AIConceptGenerator
from email_template import EmailTemplate
from email_sender import EmailSender


def main():
    """Main execution function for daily AI concepts email"""
    
    print("=" * 50)
    print("AI INSIGHT DAILY - Starting Daily Email Process")
    print("=" * 50)
    
    try:
        # Step 1: Validate configuration
        print("\n[1/6] Validating configuration...")
        config.validate()
        print("✅ Configuration validated successfully")
        
        # Step 2: Initialize storage
        print("\n[2/6] Initializing storage...")
        storage = ConceptStorage(config.storage_file)
        previous_concepts = storage.get_recent_concepts(count=50)
        print(f"✅ Loaded {len(previous_concepts)} previously sent concepts")
        
        # Step 3: Generate new AI concepts
        print("\n[3/6] Generating 5 new AI concepts...")
        ai_generator = AIConceptGenerator(
            api_key=config.perplexity_api_key,
            api_url=config.api_base_url,
            model=config.model_name,
            max_tokens=config.max_tokens,
            temperature=config.temperature
        )
        
        concepts_text = ai_generator.generate_concepts(previous_concepts)
        new_concepts = ai_generator.extract_concept_titles(concepts_text)
        print(f"✅ Generated concepts: {new_concepts[:3]}..." if len(new_concepts) > 3 else f"✅ Generated concepts: {new_concepts}")
        
        # Step 4: Create beautiful HTML email
        print("\n[4/6] Creating HTML email template...")
        html_email = EmailTemplate.create_html_email(concepts_text)
        print("✅ Email template created")
        
        # Step 5: Send email
        print("\n[5/6] Sending email...")
        email_sender = EmailSender(
            smtp_server=config.smtp_server,
            smtp_port=config.smtp_port,
            from_email=config.from_email,
            app_password=config.app_password
        )
        
        email_sender.send_html_email(
            to_email=config.to_email,
            subject=config.email_subject,
            html_content=html_email
        )
        print(f"✅ Email sent successfully to {config.to_email}")
        
        # Step 6: Update storage
        print("\n[6/6] Updating concept storage...")
        storage.add_concepts(new_concepts, max_stored=config.max_stored_concepts)
        total_concepts = len(storage.load_concepts())
        print(f"✅ Storage updated. Total concepts tracked: {total_concepts}")
        
        print("\n" + "=" * 50)
        print("✅ DAILY EMAIL SENT SUCCESSFULLY!")
        print("=" * 50)
        
        return 0
        
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
