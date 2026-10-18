public class VulnerableApp {
    String password = "admin123";
    String apiKey = "sk-live-4f8c9a";

    void run(String code, String host, String name) {
        engine.eval(code);
        Runtime.getRuntime().exec("ping " + host);
        new ProcessBuilder("sh", "-c", "ping " + host);
        stmt.execute("SELECT * FROM users WHERE name = '" + name + "'");
    }
}
