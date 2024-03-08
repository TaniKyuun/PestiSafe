from website import create_app

app = create_app()

if __name__ == "__main__":
    # Remove debug=True when deploying to production
    app.run(debug=True)
