def search_by_disease(patients, disease):
    return [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]

if __name__ == "__main__":
    patients = []
    n = int(input("Enter number of patients: "))
    for _ in range(n):
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        disease = input("Enter disease: ")
        patients.append({"Name": name, "Age": age, "Disease": disease})

    disease = input("Enter disease to search: ")
    result = search_by_disease(patients, disease)
    print(f"Patients with {disease}: {result}")
