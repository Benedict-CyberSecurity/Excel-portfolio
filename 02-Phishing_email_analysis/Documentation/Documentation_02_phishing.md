# Project 2 — Phishing Email Analysis Project
## Process
### Phase 1: Data transformation
1. Used Power Query to extract date and time information
1. Used Power Query to add framework rates and seriousness scales to the logs (from below)
1. Loaded to data model on a new workseet named tbl_logs

### Phase 2: The Framework References
1. Under a new sheet called Framework References, created tables with weighted scores. 
    - Targeted_Department: Executive obviously is more impactful than sales
    - Employee Action: dowloading an attachment is significantly more worrisome than deleting - reporting to IT is best
    - A scoring grid which rates the seriousness of each action as a product of Department importance and Employee response and assigned a NIST framework rating

### Phase 3: The Calculations
1. Using pivot tables, created frequency analysis tables
    - Finance was hardest hit with 50.44% of attack (2522 out of 5000)
1. Much more interesting was the breach analysis (breaching being defined as clicked link or downloaded attachment)
    - Sales had a 35.71% breach rate!
    - More importantly Finance was successfully breached 369 times
1. An important thing I discovered was that by looking at aggregate scores I was missing an important factor, so I searched for which department had the maximum exposure or maximum seriousness
    - Executive had 76 breaches of BEC/Whaling for a rating of very high/critical of 25
    - Urgent Invoice was a very successful attack strategy (49.82% of successful breaches fell in this category) suggesting further training and controls specifically in this area
1. In this particular set of data, time didn't appear to play any significant role
1. The good news was that 39% of attacks were ignored, 28% deleted, and 17% reported to IT. 
    - I suggest rewarding employees for reporting suspicious emails to IT to further encourage this behavior and to incentivize security awareness
### Phase 4: Summary Dashboard
1. My goal here was to present the information simply and clearly while recognizing that there were 3 different areas of concern:
    - The considerable volume of attack aimed at Finance
    - The very high rate of breach by Sales employees
    - The seriousness and impact of Executive breaches
### Phase 5: Summary Report
- A concise summary of the scope and methods employed in the analysis, the key findings, the underlying frameworks, interpretation, and  recommendations.

## Self Assessment
1. I was much more organized in this project though I can still do better with the layout of my calculations.
1. I found it useful to make informal notes along side the calculations to cement my understanding of the numbers I was seeing and to guide my next step.
1. It was an important step for me to see for myself the completely different stories seriousness scales and maximum scores (rather than average scores which hide important numbers) could tell. This really informs me moving forward.
1. It was very useful for my own learning and understanding of cyber principles and frameworks to tie data to frameworks - to see how theory and data work together to communciate complex situations really clearly.
1. I still need to improve my design or visualization skills - I think the data I am presenting is good and my analysis is meaningful but my presentation skills need more work.
1. One final thing to note is that because I used tables and formulas (nothing is hard coded), this workbook could be used as a template for analyzing other phishing logs. With some tweaks and refinements, it could be quite useful.