library(httr)
library(rvest)

# Step 1: Fetch the Wikipedia page
get_wiki_covid19_page <- function() {
    url <- 'https://en.wikipedia.org/w/index.php?title=Template:COVID-19_testing_by_country'
    response <- GET(url)
    if (status_code(response) == 200) {
        page_content <- content(response, as = "text")
        return(page_content)
    } else {
        stop("Failed to retrieve the page. Status code: ", status_code(response))
    }    
}

# Step 2: Parse the HTML and extract the table
html_text <- get_wiki_covid19_page()
html_doc <- read_html(html_text)
table_node <- html_node(html_doc, "table.wikitable")
table_data <- html_table(table_node, fill = TRUE)

# Step 3: Clean and preprocess the data
preprocessed_covid_data_frame <- function(table_data) {
    # Remove the 'World' row if it exists
    table_data <- table_data[!(table_data$`Country or region` == "World"), ]

    # Remove unnecessary columns (check if they exist first to avoid errors)
    table_data$`Ref.` <- NULL
    if ("Units[b]" %in% names(table_data)) {
        table_data$`Units[b]` <- NULL
    }

    # Rename columns for clarity
    names(table_data) <- c("country", "date", "tested", "confirmed",
                           "confirmed_tested_ratio", "tested_population_ratio",
                           "confirmed_population_ratio")

    # Convert column types
    table_data$country <- as.factor(table_data$country)
    table_data$date <- as.factor(table_data$date)
    table_data$tested <- as.numeric(gsub(",", "", table_data$tested))
    table_data$confirmed <- as.numeric(gsub(",", "", table_data$confirmed))
    table_data$confirmed_tested_ratio <- as.numeric(gsub("%", "", gsub(",", "", table_data$confirmed_tested_ratio)))
    table_data$tested_population_ratio <- as.numeric(gsub(",", "", table_data$tested_population_ratio))
    table_data$confirmed_population_ratio <- as.numeric(gsub(",", "", table_data$confirmed_population_ratio))

    return(table_data)
}

# Step 4: Apply preprocessing and view data
covid_data <- preprocessed_covid_data_frame(table_data)
csv.write(covid_data, file = "covid19_testing_by_country.csv", row.names = FALSE)
