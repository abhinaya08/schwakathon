## app.R ##
library(shiny)
library(shinydashboard)
library(DT)
library(plotly)

setwd("~/Schwathon/Shiny App/schwathon")

ui <- dashboardPage(title = "Schawab Customer Pulse",skin = "blue",
  dashboardHeader(title = tags$a(href='https://www.schwab.com/',
                                 tags$img(src='logo.png',height='60',width='60'))),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Dashboard", tabName = "dashboard", icon = icon("dashboard")),
      menuItem("Recommendations", tabName = "Recommendations", icon = icon("th")),
      menuItem("Questionnaire", tabName = "question", icon = icon("question"))
  )),
  dashboardBody(
    tags$head(tags$style(HTML(
      '.myClass { 
      font-size: 20px;
      line-height: 50px;
      text-align: left;
      font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
      padding: 0 15px;
      overflow: hidden;
      color: white;
      }
      '))),
    tags$script(HTML('
                     $(document).ready(function() {
                     $("header").find("nav").append(\'<span class="myClass"> Welcome Mark! </span>\');
                     })
                     ')),
    tags$head( 
      tags$style(HTML(".main-sidebar { font-size: 20px; }")) #change the font size to 20
    ),
    tabItems(
      # First tab content
      tabItem(tabName = "dashboard",
              h2("Portfolio for Jon Doe"),
                #infoBox("New Orders", 10 * 2, icon = icon("credit-card"), fill = TRUE),
                valueBox("$20 M", "Total Asset Value", icon = icon("credit-card")),
                valueBoxOutput("progressBox"),
                valueBoxOutput("approvalBox"),
              fluidRow(
                box(
                  title = tags$b("AAPL"), status = "primary", solidHeader = TRUE,
                  collapsible = TRUE,width = 5,collapsed = TRUE,
                  imageOutput("image1")
                ),
                box(
                  title = tags$b("FB"), status = "primary", solidHeader = TRUE,
                  collapsible = TRUE,width = 5,collapsed = TRUE,
                  imageOutput("image2")
                )),
              fluidRow(
                box(
                  title = tags$b("NVDA"), status = "primary", solidHeader = TRUE,
                  collapsible = TRUE,width = 5,collapsed = TRUE,
                  imageOutput("image3")
                ),
                box(
                  title = tags$b("SBUX"), status = "primary", solidHeader = TRUE,
                  collapsible = TRUE,width = 5,collapsed = TRUE,
                  imageOutput("image4")
                )),
              fluidRow(
                box(
                  title = tags$b("JNJ"), status = "primary", solidHeader = TRUE,
                  collapsible = TRUE,width = 5,collapsed = TRUE,
                  imageOutput("image5")
                ),
                box(
                  title = tags$b("MO"), status = "primary", solidHeader = TRUE,
                  collapsible = TRUE,width = 5,collapsed = TRUE,
                  imageOutput("image6")
                )),
                
                fluidRow(
                box(
                  title = tags$b("Financial and Social Chatter"), status = "success", solidHeader = TRUE,
                  collapsible = TRUE,width = 12,collapsed = FALSE,
                  DT::dataTableOutput("mytable")
                  #uiOutput('textWithHTML')
                )
              ),
              fluidRow(
                box(
                  title = tags$b("Portfolio Simulation: Shrinking Interest Rate (-8%~ -1%)"), status = "warning", solidHeader = TRUE,
                  collapsible = TRUE,width = 12,collapsed = TRUE,
                  plotlyOutput("revenuebyRegion", height = "300px")
                  #h5("Click button to get trends for client's owned stocks"),
                  
                )
              ),
              
              fluidRow(
                box(
                  title = tags$b("Portfolio Simulation: Moderately Shrinking Interest Rate (-1%~0)"), status = "warning", solidHeader = TRUE,
                  collapsible = TRUE,width = 12,collapsed = TRUE,
                  plotlyOutput("V2", height = "300px")
                  #h5("Click button to get trends for client's owned stocks"),
                  
                )
              ),
              fluidRow(
                box(
                  title = tags$b("Portfolio Simulation: Moderately Growing Interest Rate (0~1%)"), status = "warning", solidHeader = TRUE,
                  collapsible = TRUE,width = 12,collapsed = TRUE,
                  plotlyOutput("V3", height = "300px")
                  #h5("Click button to get trends for client's owned stocks"),
                  
                )
              ),
              fluidRow(
                box(
                  title = tags$b("Portfolio Simulation: Growing Interest Rate (1%~14%)"), status = "warning", solidHeader = TRUE,
                  collapsible = TRUE,width = 12,collapsed = TRUE,
                  plotlyOutput("V4", height = "300px")
                  #h5("Click button to get trends for client's owned stocks"),
                  
                )
              )
      ),
      tabItem(tabName = "Recommendations",
              h2 ("Marketing Recommendations"),
              h4("Since the client has a high probability to retire soon, we recommend initiaing conversations
                 about IRAs with him.")
              ),
              tabItem(tabName = "question",
                      h2 ("Questionnaire"),
                      includeHTML("questionnaire.html")
      )
    )
  )
)
  

server <- function(input, output) { 
  output$progressBox <- renderValueBox({
    valueBox( "25%", "Risk", icon = icon("thumbs-up", lib = "glyphicon"),
      color = "purple"
    )
  })
  
  output$approvalBox <- renderValueBox({
    valueBox(
      "80%", "Probability of Early Retirement", icon = icon("user", lib = "glyphicon"),
      color = "maroon"
    )
  })
  
    output$image1 <- renderImage({
      list(src="www/AAPL.png")
    }, deleteFile = FALSE) 
    
    output$image2 <- renderImage({
      list(src="www/FB.png")
    }, deleteFile = FALSE) 

    output$image3 <- renderImage({
      list(src="www/NVDA.png")
    }, deleteFile = FALSE) 
    
  
    output$image4 <- renderImage({
      list(src="www/SBUX.png")
    }, deleteFile = FALSE) 
    
    output$image5 <- renderImage({
      list(src="www/JNJ.png")
    }, deleteFile = FALSE) 
    
    output$image6 <- renderImage({
      list(src="www/MO.png")
    }, deleteFile = FALSE) 
    
    output$mytable = DT::renderDataTable({
      df <- read.csv("topics.csv")
      #names(df) <- "Topics"
      df
    })
    
    output$revenuebyRegion <- renderPlotly({
      f <- list(
        family = "Courier New, monospace",
        size = 18,
        color = "#7f7f7f"
      )
      x <- list(
        title = "Return when principle = $100000",
        titlefont = f
      )
      y <- list(
        title = "Density",
        titlefont = f
      )
      recommendation <- read.csv("return_simulation_5range_interest.csv")
      plot_ly(recommendation, x = ~V1,type="histogram") %>%
        layout(xaxis = x, yaxis = y)
    })
    
    output$V2 <- renderPlotly({
      f <- list(
        family = "Courier New, monospace",
        size = 18,
        color = "#7f7f7f"
      )
      x <- list(
        title = "Return when principle = $100000",
        titlefont = f
      )
      y <- list(
        title = "Density",
        titlefont = f
      )
      recommendation <- read.csv("return_simulation_5range_interest.csv")
      plot_ly(recommendation, x = ~V2,type="histogram") %>%
        layout(xaxis = x, yaxis = y)
    })
    
    output$V3 <- renderPlotly({
      f <- list(
        family = "Courier New, monospace",
        size = 18,
        color = "#7f7f7f"
      )
      x <- list(
        title = "Return when principle = $100000",
        titlefont = f
      )
      y <- list(
        title = "Density",
        titlefont = f
      )
      recommendation <- read.csv("return_simulation_5range_interest.csv")
      plot_ly(recommendation, x = ~V3,type="histogram") %>%
        layout(xaxis = x, yaxis = y)
    })
    
    output$V4 <- renderPlotly({
      f <- list(
        family = "Courier New, monospace",
        size = 18,
        color = "#7f7f7f"
      )
      x <- list(
        title = "Return when principle = $100000",
        titlefont = f
      )
      y <- list(
        title = "Density",
        titlefont = f
      )
      recommendation <- read.csv("return_simulation_5range_interest.csv")
      plot_ly(recommendation, x = ~V4,type="histogram") %>%
        layout(xaxis = x, yaxis = y)
    })
    
  }

shinyApp(ui, server)