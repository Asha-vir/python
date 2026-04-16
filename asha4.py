#include <iostream>
#include <string>

using namespace std;

// Define the struct named Student
struct Student {
    int age;
    string first_name;
    string last_name;
    int standard;
};

int main() {
    Student st;
    
    // Reading input from stdin
    cin >> st.age >> st.first_name >> st.last_name >> st.standard;
    
    // Printing the space-separated output
    cout << st.age << " " << st.first_name << " " << st.last_name << " " << st.standard;
    
    return 0;
}
