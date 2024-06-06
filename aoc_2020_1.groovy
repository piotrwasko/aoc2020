def TARGET_SUM = 2020
def results = new HashMap<Integer, Integer>()

def input = new File("./1.input.txt").readLines().collect {Integer.parseInt(it) }

for (int i = 0; i < input.size(); i++) {
    for (int j = i; j < input.size(); j++) {
        results[input[i] + input[j]] = input[i] * input[j]
    }
}

for (def num in input) {
    if (results.containsKey(TARGET_SUM - num)) {
        println(num * results[TARGET_SUM - num])
        return
    }
}
