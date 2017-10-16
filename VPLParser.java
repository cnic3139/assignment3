// Generated from VPL.g by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, FUNC=13, END=14, VAR=15, IF=16, WHILE=17, 
		THEN=18, DO=19, ENDIF=20, ENDWHILE=21, IDENT=22, NUM=23;
	public static final int
		RULE_start = 0, RULE_m = 1, RULE_f = 2, RULE_p = 3, RULE_l = 4, RULE_d = 5, 
		RULE_s = 6, RULE_r = 7, RULE_e = 8, RULE_c = 9;
	public static final String[] ruleNames = {
		"start", "m", "f", "p", "l", "d", "s", "r", "e", "c"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'('", "')'", "','", "';'", "'='", "'add'", "'minus'", "'mult'", 
		"'div'", "'min'", "'<'", "'>'", "'func'", "'end'", "'var'", "'if'", null, 
		"'then'", "'do'", null, "'endwhile'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, "FUNC", "END", "VAR", "IF", "WHILE", "THEN", "DO", "ENDIF", "ENDWHILE", 
		"IDENT", "NUM"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "VPL.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public VPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class StartContext extends ParserRuleContext {
		public MContext m() {
			return getRuleContext(MContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			m();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MContext extends ParserRuleContext {
		public FContext f() {
			return getRuleContext(FContext.class,0);
		}
		public MContext m() {
			return getRuleContext(MContext.class,0);
		}
		public MContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_m; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterM(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitM(this);
		}
	}

	public final MContext m() throws RecognitionException {
		MContext _localctx = new MContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_m);
		try {
			setState(26);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNC:
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				f();
				setState(23);
				m();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(VPLParser.FUNC, 0); }
		public TerminalNode IDENT() { return getToken(VPLParser.IDENT, 0); }
		public PContext p() {
			return getRuleContext(PContext.class,0);
		}
		public DContext d() {
			return getRuleContext(DContext.class,0);
		}
		public SContext s() {
			return getRuleContext(SContext.class,0);
		}
		public TerminalNode END() { return getToken(VPLParser.END, 0); }
		public FContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterF(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitF(this);
		}
	}

	public final FContext f() throws RecognitionException {
		FContext _localctx = new FContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_f);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(FUNC);
			setState(29);
			match(IDENT);
			setState(30);
			p();
			setState(31);
			d();
			setState(32);
			s();
			setState(33);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PContext extends ParserRuleContext {
		public LContext l() {
			return getRuleContext(LContext.class,0);
		}
		public PContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_p; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitP(this);
		}
	}

	public final PContext p() throws RecognitionException {
		PContext _localctx = new PContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_p);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(T__0);
			setState(36);
			l();
			setState(37);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(VPLParser.IDENT, 0); }
		public LContext l() {
			return getRuleContext(LContext.class,0);
		}
		public LContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterL(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitL(this);
		}
	}

	public final LContext l() throws RecognitionException {
		LContext _localctx = new LContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_l);
		try {
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				match(IDENT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(40);
				match(IDENT);
				setState(41);
				match(T__2);
				setState(42);
				l();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DContext extends ParserRuleContext {
		public LContext l() {
			return getRuleContext(LContext.class,0);
		}
		public DContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_d; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterD(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitD(this);
		}
	}

	public final DContext d() throws RecognitionException {
		DContext _localctx = new DContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_d);
		try {
			setState(50);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				match(VAR);
				setState(46);
				l();
				setState(47);
				match(T__3);
				}
				break;
			case T__3:
			case END:
			case IF:
			case WHILE:
			case IDENT:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(VPLParser.IF, 0); }
		public CContext c() {
			return getRuleContext(CContext.class,0);
		}
		public TerminalNode THEN() { return getToken(VPLParser.THEN, 0); }
		public SContext s() {
			return getRuleContext(SContext.class,0);
		}
		public TerminalNode ENDIF() { return getToken(VPLParser.ENDIF, 0); }
		public RContext r() {
			return getRuleContext(RContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(VPLParser.WHILE, 0); }
		public TerminalNode DO() { return getToken(VPLParser.DO, 0); }
		public TerminalNode ENDWHILE() { return getToken(VPLParser.ENDWHILE, 0); }
		public TerminalNode IDENT() { return getToken(VPLParser.IDENT, 0); }
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public SContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterS(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitS(this);
		}
	}

	public final SContext s() throws RecognitionException {
		SContext _localctx = new SContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_s);
		try {
			setState(72);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				match(IF);
				setState(53);
				c();
				setState(54);
				match(THEN);
				setState(55);
				s();
				setState(56);
				match(ENDIF);
				setState(57);
				r();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				match(WHILE);
				setState(60);
				c();
				setState(61);
				match(DO);
				setState(62);
				s();
				setState(63);
				match(ENDWHILE);
				setState(64);
				r();
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 3);
				{
				setState(66);
				match(IDENT);
				setState(67);
				match(T__4);
				setState(68);
				e();
				setState(69);
				r();
				}
				break;
			case T__3:
			case END:
			case ENDIF:
			case ENDWHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(71);
				r();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RContext extends ParserRuleContext {
		public SContext s() {
			return getRuleContext(SContext.class,0);
		}
		public RContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_r; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterR(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitR(this);
		}
	}

	public final RContext r() throws RecognitionException {
		RContext _localctx = new RContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_r);
		try {
			setState(77);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				match(T__3);
				setState(75);
				s();
				}
				break;
			case END:
			case ENDIF:
			case ENDWHILE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EContext extends ParserRuleContext {
		public List<EContext> e() {
			return getRuleContexts(EContext.class);
		}
		public EContext e(int i) {
			return getRuleContext(EContext.class,i);
		}
		public TerminalNode IDENT() { return getToken(VPLParser.IDENT, 0); }
		public TerminalNode NUM() { return getToken(VPLParser.NUM, 0); }
		public EContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterE(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitE(this);
		}
	}

	public final EContext e() throws RecognitionException {
		EContext _localctx = new EContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_e);
		try {
			setState(120);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				match(T__5);
				setState(80);
				match(T__0);
				setState(81);
				e();
				setState(82);
				match(T__2);
				setState(83);
				e();
				setState(84);
				match(T__1);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				match(T__6);
				setState(87);
				match(T__0);
				setState(88);
				e();
				setState(89);
				match(T__2);
				setState(90);
				e();
				setState(91);
				match(T__1);
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(93);
				match(T__7);
				setState(94);
				match(T__0);
				setState(95);
				e();
				setState(96);
				match(T__2);
				setState(97);
				e();
				setState(98);
				match(T__1);
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 4);
				{
				setState(100);
				match(T__8);
				setState(101);
				match(T__0);
				setState(102);
				e();
				setState(103);
				match(T__2);
				setState(104);
				e();
				setState(105);
				match(T__1);
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 5);
				{
				setState(107);
				match(T__9);
				setState(108);
				match(T__0);
				setState(109);
				e();
				setState(110);
				match(T__2);
				setState(111);
				e();
				setState(112);
				match(T__1);
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 6);
				{
				setState(114);
				match(T__0);
				setState(115);
				e();
				setState(116);
				match(T__1);
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 7);
				{
				setState(118);
				match(IDENT);
				}
				break;
			case NUM:
				enterOuterAlt(_localctx, 8);
				{
				setState(119);
				match(NUM);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CContext extends ParserRuleContext {
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public TerminalNode NUM() { return getToken(VPLParser.NUM, 0); }
		public CContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_c; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).enterC(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VPLListener ) ((VPLListener)listener).exitC(this);
		}
	}

	public final CContext c() throws RecognitionException {
		CContext _localctx = new CContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_c);
		try {
			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(122);
				e();
				setState(123);
				match(T__10);
				setState(124);
				match(NUM);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(126);
				e();
				setState(127);
				match(T__11);
				setState(128);
				match(NUM);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31\u0087\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\3\2\3\2\3\3\3\3\3\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6.\n\6\3\7\3\7\3\7\3\7\3\7\5\7\65\n\7"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\5\bK\n\b\3\t\3\t\3\t\5\tP\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n{"+
		"\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0085\n\13\3\13\2\2"+
		"\f\2\4\6\b\n\f\16\20\22\24\2\2\2\u008b\2\26\3\2\2\2\4\34\3\2\2\2\6\36"+
		"\3\2\2\2\b%\3\2\2\2\n-\3\2\2\2\f\64\3\2\2\2\16J\3\2\2\2\20O\3\2\2\2\22"+
		"z\3\2\2\2\24\u0084\3\2\2\2\26\27\5\4\3\2\27\3\3\2\2\2\30\31\5\6\4\2\31"+
		"\32\5\4\3\2\32\35\3\2\2\2\33\35\3\2\2\2\34\30\3\2\2\2\34\33\3\2\2\2\35"+
		"\5\3\2\2\2\36\37\7\17\2\2\37 \7\30\2\2 !\5\b\5\2!\"\5\f\7\2\"#\5\16\b"+
		"\2#$\7\20\2\2$\7\3\2\2\2%&\7\3\2\2&\'\5\n\6\2\'(\7\4\2\2(\t\3\2\2\2)."+
		"\7\30\2\2*+\7\30\2\2+,\7\5\2\2,.\5\n\6\2-)\3\2\2\2-*\3\2\2\2.\13\3\2\2"+
		"\2/\60\7\21\2\2\60\61\5\n\6\2\61\62\7\6\2\2\62\65\3\2\2\2\63\65\3\2\2"+
		"\2\64/\3\2\2\2\64\63\3\2\2\2\65\r\3\2\2\2\66\67\7\22\2\2\678\5\24\13\2"+
		"89\7\24\2\29:\5\16\b\2:;\7\26\2\2;<\5\20\t\2<K\3\2\2\2=>\7\23\2\2>?\5"+
		"\24\13\2?@\7\25\2\2@A\5\16\b\2AB\7\27\2\2BC\5\20\t\2CK\3\2\2\2DE\7\30"+
		"\2\2EF\7\7\2\2FG\5\22\n\2GH\5\20\t\2HK\3\2\2\2IK\5\20\t\2J\66\3\2\2\2"+
		"J=\3\2\2\2JD\3\2\2\2JI\3\2\2\2K\17\3\2\2\2LM\7\6\2\2MP\5\16\b\2NP\3\2"+
		"\2\2OL\3\2\2\2ON\3\2\2\2P\21\3\2\2\2QR\7\b\2\2RS\7\3\2\2ST\5\22\n\2TU"+
		"\7\5\2\2UV\5\22\n\2VW\7\4\2\2W{\3\2\2\2XY\7\t\2\2YZ\7\3\2\2Z[\5\22\n\2"+
		"[\\\7\5\2\2\\]\5\22\n\2]^\7\4\2\2^{\3\2\2\2_`\7\n\2\2`a\7\3\2\2ab\5\22"+
		"\n\2bc\7\5\2\2cd\5\22\n\2de\7\4\2\2e{\3\2\2\2fg\7\13\2\2gh\7\3\2\2hi\5"+
		"\22\n\2ij\7\5\2\2jk\5\22\n\2kl\7\4\2\2l{\3\2\2\2mn\7\f\2\2no\7\3\2\2o"+
		"p\5\22\n\2pq\7\5\2\2qr\5\22\n\2rs\7\4\2\2s{\3\2\2\2tu\7\3\2\2uv\5\22\n"+
		"\2vw\7\4\2\2w{\3\2\2\2x{\7\30\2\2y{\7\31\2\2zQ\3\2\2\2zX\3\2\2\2z_\3\2"+
		"\2\2zf\3\2\2\2zm\3\2\2\2zt\3\2\2\2zx\3\2\2\2zy\3\2\2\2{\23\3\2\2\2|}\5"+
		"\22\n\2}~\7\r\2\2~\177\7\31\2\2\177\u0085\3\2\2\2\u0080\u0081\5\22\n\2"+
		"\u0081\u0082\7\16\2\2\u0082\u0083\7\31\2\2\u0083\u0085\3\2\2\2\u0084|"+
		"\3\2\2\2\u0084\u0080\3\2\2\2\u0085\25\3\2\2\2\t\34-\64JOz\u0084";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}