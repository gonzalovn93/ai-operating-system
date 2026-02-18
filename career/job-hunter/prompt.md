# JobHunter — Workflow Prompt

## Purpose
Automatically scrape career pages of Tier 1 target companies, find Product Manager roles, and add them to a Notion Applications database.

## Core Functionality

### Input
- Tier 1 companies list from Companies DB (Strategic Tier = "T1—Priority Target")
- Career page URLs from config

### Processing
1. Scrape each company's career page daily
2. Filter for PM roles (exclude TPM, Group PM)
3. Extract: Job title, location, URL, compensation (if available)
4. Check for duplicates in Applications DB
5. Add new jobs with Status="Not applied"

### Output
- New entries in Applications DB
- Daily log file
- Summary for WeeklyRecruitingMemo

## Tier 1 Companies

The system supports 16-18 target companies across multiple ATS platforms. Companies are configurable via `tier1_companies.json`. Example targets include consumer tech, AI-native startups, fintech, and sports/lifestyle brands.

## Job Title Filters

**Include (case-insensitive):**
- "Product Manager", "Senior Product Manager", "Staff Product Manager"
- "Principal Product Manager", "AI Product Manager"
- "Platform Product Manager", "Consumer Product Manager"
- "Senior PM", "Staff PM"

**Exclude:**
- "Technical Program Manager", "TPM"
- "Group Product Manager", "Group PM"
- "VP Product"
- "Director of Product" (unless also contains "Manager")

## Scraper Architecture

### Base Scraper Class
```python
class BaseCareerScraper:
    def __init__(self, company_name, career_url):
        self.company_name = company_name
        self.career_url = career_url

    def scrape(self):
        """Must be implemented by each company scraper"""
        raise NotImplementedError

    def filter_pm_roles(self, jobs):
        """Filters jobs for PM roles only"""

    def extract_job_data(self, job_element):
        """Extract structured data from job posting"""
        # Returns: {title, location, url, compensation}
```

### ATS-Specific Scrapers
Each company needs a custom scraper due to different ATS platforms and page structures. Supported ATS types include:
- **Greenhouse** — JSON API at `boards.greenhouse.io/{company}`
- **Ashby** — JavaScript-heavy pages at `jobs.ashbyhq.com/{company}`
- **Lever** — BeautifulSoup-friendly pages at `jobs.lever.co/{company}`
- **Workday** — Custom React apps with JSON endpoints
- **Eightfold** — API-based job listings
- **TalentBrew** — Standard job board scraping
- **Manual SPA** — LinkedIn job search fallback for companies with custom career sites

### Notion Integration

**Write to Applications DB:**
```python
notion.pages.create(
    parent={"database_id": "your-notion-db-id"},
    properties={
        "Position": {"title": [{"text": {"content": job_title}}]},
        "Company": {"relation": [{"id": company_page_id}]},
        "Type": {"select": {"name": "Full time"}},
        "Stage": {"select": {"name": "Open"}},
        "Status": {"status": {"name": "Not applied"}},
        "Link": {"url": job_url},
        "Location": {"rich_text": [{"text": {"content": location}}]},
        "Application Posted": {
            "date": {"start": datetime.now().isoformat()}
        }
    }
)
```

**Deduplication Check:**
```python
existing = notion.databases.query(
    database_id="your-notion-db-id",
    filter={"property": "Link", "url": {"equals": job_url}}
)
if existing["results"]:
    return  # Skip duplicate
```

## Error Handling

```python
def scrape_with_retry(scraper, max_retries=3):
    for attempt in range(max_retries):
        try:
            return scraper.scrape()
        except Exception as e:
            if attempt == max_retries - 1:
                log_error(f"Failed after {max_retries} attempts: {e}")
                return []
            time.sleep(5)
```

## Usage

```bash
python main.py hunt                              # Full run
python main.py hunt --test --company="Company"   # Test single company
python main.py hunt --dry-run                     # Preview only
python main.py hunt --json                        # Structured output
```

## Output Summary Format

```json
{
  "week": "2026-02-04",
  "jobs_found": 12,
  "jobs_added": 9,
  "by_company": {"Company A": 3, "Company B": 2},
  "closing_soon": [
    {"company": "Company A", "role": "AI PM", "closes": "2026-02-14", "days_remaining": 10}
  ]
}
```

## File Structure

```
workflows/job_hunter/
├── job_hunter.py          # Main orchestrator
├── linkedin_job_search.py # LinkedIn fallback
├── expertise_filter.py    # PM role scoring
├── scrapers/
│   ├── base_scraper.py
│   └── {ats}_scraper.py   # One per ATS type
└── tests/
```

## Success Criteria

- Scrapes all Tier 1 companies successfully
- Finds PM roles and filters accurately
- Adds new jobs to Applications DB
- Skips duplicates
- Logs all activities
- Generates summary for WeeklyRecruitingMemo

## Known Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| JavaScript-heavy career pages | Selenium with explicit waits |
| Rate limiting / bot detection | Delays between requests, rotate user agents |
| Page structure changes | Graceful degradation, log errors, continue |
| Compensation data not always available | Make field optional |
