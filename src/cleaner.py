import pandas as pd

class DataCleaner:
    def clean(self, ab: pd.DataFrame) -> pd.DataFrame:

        ab = ab.copy()

        
        ab = ab.dropna(how="all")

        
        ab = ab.drop_duplicates()

        
        ab.columns = (
            ab.columns
            .str.strip()
            .str.lower()
            .str.replace(" ","_")
        )


        
        for column in ab.select_dtypes(include="object").columns:
            ab[column] = ab[column].astype(str).str.strip()

        
        if "date" in ab.columns:
            ab["date"] = pd.to_datetime(
                ab["date"],
                errors="coerce"
            )

        
        numeric_colums = [
            "sales",
            "quantity",
            "profit"
        ]

        for column in numeric_colums:
            if column in ab.columns:
                ab[column] = pd.to_numeric(
                    ab[column],
                    errors="coerce"
                )

        
        required_columns = [
            "sales",
            "quantity",
            "profit"
        ]

        existing_columns = [
            col for col in required_columns
            if col in ab.columns
        ]

        ab = ab.dropna(subset=existing_columns)

        return ab