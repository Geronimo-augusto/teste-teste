public class VulnerableApp {
    string password = "admin123";
    void Run(string code, string host, string name) {
        Process.Start("ping " + host);
        new ProcessStartInfo("cmd", "/c ping " + host);
        cmd.ExecuteReader("SELECT * FROM users WHERE name = '" + name + "'");
    }
}