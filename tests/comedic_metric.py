# %%
jokescore = "{\"comedic_value\": 3, \"relevance\": 2}"


# %%
import json
def line_process(jokescore: str):
    """
    This tool processes the prediction of a single line and returns the processed result.

    :param groundtruth: the groundtruth of a single line.
    :param prediction: the prediction of a single line.
    """
    jokescore_json = json.loads(jokescore)

    jokescore_dict = dict(jokescore_json)

    return jokescore_dict




# %%
result = line_process(jokescore)

# %%
print(result['comedic_value'])
print(result['relevance'])

# %%
processed_results = [result, result, result]

print(processed_results)

aggregated_results = {}

for m in processed_results:
    # if aggregated_results.
    for k,v  in m.items():
        print(f"key={k}, value={v}")
        if aggregated_results.get(k) is None:

            print(f"{k} is none")
            aggregated_results[k] = [v]
        else:
            aggregated_results[k].append(v)

print(aggregated_results)

# %%


# %%
aggregated_results['comedic_value'].append(4)

# %%
aggregated_results


# %%



