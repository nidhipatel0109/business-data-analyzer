import pandas as pd

class BusinessAnalyzer:

    def __init__(self,ab: pd.DataFrame):
        self.ab = ab

    def total_sales(self):
        return self.ab["sales"].sum()

    def total_profit(self):
        return self.ab["profit"].sum()

    def total_quantity(self):
        return self.ab["quantity"].sum()

    def average_sales(self):
        return self.ab["sales"].mean()

    def profit_margin(self):

        total_sales = self.total_sales()

        if total_sales == 0:
            return 0

        return(
            self.total_profit()
            /total_sales
        ) * 100

    def best_product(self):

        product_sales = (
            self.ab
            .groupby("product")["sales"]
            .sum()
        )

        return product_sales.idxmax()

    def best_region(self):

        region_sales = (
            self.ab
            .groupby("region")["sales"]
            .sum()
        )

        return region_sales.idxmax()

    def product_summary(self):

        return(
            self.ab
            .groupby("product")
            .agg(
                sales = ("sales", "sum"),
                quantity = ("quantity", "sum"),
                profit = ("profit", "sum")
            )
            .sort_values(
                "sales",
                ascending=False
            )
        )

    def region_summary(self):

        return (
            self.ab
            .groupby("region")
            .agg(
                sales = ("sales", "sum"),
                profit = ("profit", "sum")
            )
            .sort_values(
                "sales",
                ascending=False
            )
        )