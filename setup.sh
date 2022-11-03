mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"mahalelalit45@gmail.com\"\n\
"> ~/.stramlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
"> ~/.streamlit/config.toml