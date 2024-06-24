import argparse
from python_files.read_and_clean import read_csv, rename_col, clean_csv
from python_files.data_procesing import breakdown_date, erase_month
from python_files.data_clustering import groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
from python_files.visualization import time_evolution
from python_files.state_analysis import groupby_state, clean_states, read_csv2, merge_datasets, calculate_relative_values, analyze_kentucky_outlier
from python_files.choropleth_maps import open_json, create_choropleth, create_image

def main():
    parser = argparse.ArgumentParser(description='Firearm Analysis')
    parser.add_argument("--all", action="store_true", help="Run all steps")
    parser.add_argument("--read_csv", action="store_true", help="Read and clean CSV")
    parser.add_argument("--breakdown_date", action="store_true", help="Break down date")
    parser.add_argument("--erase_month", action="store_true", help="Erase month")
    parser.add_argument("--groupby_state_and_year", action="store_true", help="Group by state and year")
    parser.add_argument("--print_biggest_handguns", action="store_true", help="Print biggest handguns")
    parser.add_argument("--print_biggest_longguns", action="store_true", help="Print biggest longguns")
    parser.add_argument("--time_evolution", action="store_true", help="Time evolution")
    parser.add_argument("--groupby_state", action="store_true", help="Group by state")
    parser.add_argument("--clean_states", action="store_true", help="Clean states")
    parser.add_argument("--read_csv2", action="store_true", help="Read CSV 2")
    parser.add_argument("--merge_datasets", action="store_true", help="Merge datasets")
    parser.add_argument("--calculate_relative_values", action="store_true", help="Calculate relative values")
    parser.add_argument("--analyze_kentucky_outlier", action="store_true", help="Analyze Kentucky outlier")
    parser.add_argument("--open_json", action="store_true", help="Open JSON")
    parser.add_argument("--create_image", action="store_true", help="Create image")
    
    args = parser.parse_args()

    if args.all:
        run_all_steps()
    else:
        if args.read_csv:
            df = read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSiynPK5z9fMzxXycuKXrd54178ilBf2YKyL2MkW-MWpS3O98ianbyW5cVDCTPLlXSoBbDJSyTvusK7/pub?gid=203817388&single=true&output=csv")
            df = clean_csv(df)
            df = rename_col(df)
        if args.breakdown_date:
            df = breakdown_date(df)
        if args.erase_month:
            df = erase_month(df)
        if args.groupby_state_and_year:
            grouped_df = groupby_state_and_year(df)
        if args.print_biggest_handguns:
            print_biggest_handguns(grouped_df)
        if args.print_biggest_longguns:
            print_biggest_longguns(grouped_df)
        if args.time_evolution:
            time_evolution(df)
        if args.groupby_state:
            grouped_df = groupby_state(grouped_df)
        if args.clean_states:
            cleaned_df = clean_states(grouped_df)
        if args.read_csv2:
            df2 = read_csv2("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-UC6IPDj8fDJZQLPEfehfE6QTPK1bJUTuqCgsgdGFSm-uitpg3XXYWf6a-ZnchmSCRyFuF5tKeQNj/pub?gid=1623308884&single=true&output=csv")
        if args.merge_datasets:
            merged_df = merge_datasets(cleaned_df, df2)
        if args.calculate_relative_values:
            merged_df = calculate_relative_values(merged_df)
        if args.analyze_kentucky_outlier:
            merged_df = analyze_kentucky_outlier(merged_df)
        if args.open_json:
            state_geo = open_json("https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json")
        if args.create_image:
            create_image(merged_df, "permit_perc", "handgun_perc", "longgun_perc")

def run_all_steps():
    df = read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSiynPK5z9fMzxXycuKXrd54178ilBf2YKyL2MkW-MWpS3O98ianbyW5cVDCTPLlXSoBbDJSyTvusK7/pub?gid=203817388&single=true&output=csv")
    df = clean_csv(df)
    df = rename_col(df)
    
    df = breakdown_date(df)
    df = erase_month(df)

    grouped_df = groupby_state_and_year(df)
    print_biggest_handguns(grouped_df)
    print_biggest_longguns(grouped_df)
    
    time_evolution(df)

    grouped_df = groupby_state(grouped_df)
    cleaned_df = clean_states(grouped_df)
    df2 = read_csv2("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-UC6IPDj8fDJZQLPEfehfE6QTPK1bJUTuqCgsgdGFSm-uitpg3XXYWf6a-ZnchmSCRyFuF5tKeQNj/pub?gid=1623308884&single=true&output=csv")
    merged_df = merge_datasets(cleaned_df, df2)
    merged_df = calculate_relative_values(merged_df)
    merged_df = analyze_kentucky_outlier(merged_df)
    
    state_geo = open_json("https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json")
    create_image(merged_df, state_geo, "permit_perc", "handgun_perc", "longgun_perc")

if __name__ == '__main__':
    main()
    
# Bibliografía: https://docs.python.org/es/3/library/argparse.html
# https://ellibrodepython.com/python-argparse
# https://github.com/pytorch/examples/blob/main/imagenet/main.py
# https://docs.python.org/es/3/library/__main__.html