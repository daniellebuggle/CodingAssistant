import com.github.javaparser.*;
import com.github.javaparser.ast.*;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.stmt.*;
import com.github.javaparser.ast.expr.*;

import java.util.*;

public class ASTParser {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java ASTParser <code> <statementType>");
            return;
        }

        String code = args[0];  // Accept Java code as an argument
        String statementType = args[1];  // Accept the type of statement to check for

        JavaParser parser = new JavaParser();
        ParseResult<CompilationUnit> result = parser.parse(code);

        if (result.isSuccessful() && result.getResult().isPresent()) {
            CompilationUnit cu = result.getResult().get();

            boolean containsStatement = false;

            // Check based on the provided statement type
            switch (statementType) {
                case "Java While-Loop":
                    containsStatement = cu.findAll(WhileStmt.class).size() > 0;
                    break;
                case "Java For-Loop":
                    containsStatement = cu.findAll(ForStmt.class).size() > 0;
                    break;
                case "Java If-Else":
                    containsStatement = cu.findAll(IfStmt.class).size() > 0;
                    break;
                case "Java OR Operator":
                    containsStatement = cu.findAll(BinaryExpr.class).stream()
                            .anyMatch(expr -> expr.getOperator() == BinaryExpr.Operator.AND
                                              || expr.getOperator() == BinaryExpr.Operator.OR);
                    break;
                case "Java Do-While":
                    containsStatement = cu.findAll(DoStmt.class).size() > 0;
                    break;
                default:
                    System.out.println("Unknown statement type: " + statementType);
                    return;
            }

            // Output the result
            if (containsStatement) {
                System.out.println("The code contains a " + statementType + " statement.");
            } else {
                System.out.println("The code does not contain a " + statementType + " statement.");
            }
        } else {
            System.out.println("Parsing failed.");
        }
    }
}
