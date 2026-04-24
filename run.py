from app import create_app

app = create_app()

if __name__ == '__main__':
    # Database is managed via external database.sql script now.
    app.run(debug=True)
