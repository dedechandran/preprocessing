from app.main import app
if __name__ == "__main__":
  app.config['JSON_AS_ASCII'] = False
  app.run()