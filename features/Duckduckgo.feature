Feature: Automate a website
    Scenario: perform click events
      When visit url "https://duckduckgo.com/"
      When check if title is "DuckDuckGo — Privacy, simplified."
