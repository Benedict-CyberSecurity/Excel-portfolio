# Process Notes for 01 Sales Performance Dashboard
* Created ToDo 
* Gemini taught me how to format in Markdown
* Chose data source with the help of Notebook LM
* In Excel, created sheets for different parts of the workbook: Data, Lists, Calculations, Dashboard 
    - * later added Analysis
* Set up lists for data validation using a naming convention (tbl_ for table, l_for list)
* Examined the data to see what kinds of useful information I could pull out:
    1. **Obvious choices:**
    a. sales per region
    b. sales per salesperson
    c. sales by product
    d. sales by customer type
    e. <span style="color:blue">returns by region</span>
    f. <span style="color:blue">returns by salespeson</span>
    g. <span style="color:blue">returns of product</span>
    <span style="color:blue">(Realized that these need to be percercentages not COUNTs)</span>
    1. **More interesting analysis:**
    a. analysis of promotions (how effective? what could be more profitable?)
    b. analysis of discounts (profitable? what are the most profitable discounts?)
    c. analysis of repeat customers/purchases - what if scenarios such as promotions for repeat customers - used CONDITIONAL FORMATTING to verify there were repeat customers.
* Used SUMIFS to create sales per _ <span style="color:blue">realized this wasn't very useful for comparisions or making charts. Would be useful for summary information. I also included the delivery cost which could impact the accuracy of revenue information</span>
* Created PIVOTTABLES to explore sales
* <span style="color:green">Mistake: created a PIVTOTTABLE for delivery dates before pulling year information resulting in ugly date columns</span> Problem solved: created a helper column using YEAR.
* <span style="color:green">Problem with PIVOTTABLE: I added YEAR to the table data but the PIVOTTABLE fields were not showing me the new field YEAR</span> Simple fix! Refresh!
* <span style="color:green">Problem with the Returns by Product PIVOTTABLE. It is counting every entry in the return column because the data in the column is 0 or 1.</span> A simple fix - please see screenshots:

    1. Using FIND  and REPLACE to remove 0s and substitute with a blank
    1. Add data validation so only a 1 can be entered if the product is returned
    1. <span style="color:red">Reveals a weakness in the data structure. Currently this is setup as a binary situation (returned, not returned) when it could be quite possible for part of an order to be returned, not the entire thing. For example one item is damaged and the customer returns it for an exchange or they ordered 12 desks and only need 10.</span> Quantity and Reason would be 2 additional Return data sets I would discuss with the client to improve the usefulness of their data collection.
* Generated a couple of different types of PIVOTCHARTS to visualize PIVOTTABLES.  Please see screenshot.
* Want to create a function that replaces store alpha designations with names of cities
    1. I achieved this by creating a new PIVOTTABLE and linking the main data table with my lookup table
    1. I enabled **the data model and mapped the relationship** between columns. Please see screenshot.
* **Dashboard ideas:**
    1. Best Store in Year 
    1. Best Salesperson in Year
    1. Best selling products in Year
    1. State of returns (up or down) this Year relative to other Year
         - created PIVOTTABLES and SLICERS for each
         - using shapes and inserting an icon for a logo, laid out the design for the daskboard.
         - the goal is to make it clean and simple, easy to read and of course to function correctly
    1. Gemini suggested I should add dashboard features related to KPIs
    1. Gemini also suggested I should have a separate Analysis sheet
    1. Gemini recommended that I add a small insights or recommendations section
* In developing my dashboard, I realize that my calculations sheet is not well organized. In the future I would have an analysis sheet separate from my calculations sheet. 
* I learned a lot about troubleshooting and repairing but I didn't quite satisfy my goal.
