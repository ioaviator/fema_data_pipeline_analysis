from include.ETL.extract import extract
from include.ETL.transform import transform


def main():
  # api_data = extract()
  transformed_data = transform([])

  return True


if __name__ == '__main__':
  main()