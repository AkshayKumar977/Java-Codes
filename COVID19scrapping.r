library(httr)
library(rvest)
get_wiki_covid19_page <- function() {
    url <- 'https://en.wikipedia.org/w/index.php?title=Template:COVID-19_testing_by_country'
   
    response <- GET(url)
    if (status_code(response) == 200){
        page_content <- content(response,as = "text")
        return(page_content)
    }
    else{
        stop("Failed to retrieve the page. Status code: ",status_code(response))
    }    
}
html_text <-(get_wiki_covid19_page())
html_node <- read_html(html_text)
table_node <- html_node(html_node,"table.wikitable")
table_data <- html_table(table_node,fill = TRUE)
print(table_data)